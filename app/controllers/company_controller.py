import traceback
from datetime import datetime, timedelta

from flask import render_template, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc

import Messages
from app import app, db, Quote, UserCompanyPrivilege
from app.components.time_series import TimeSeries
from app.components.yahooApi import YahooApi
from app.models.companies_model import Company as company, Company
from app.schemas.company_schema import CompanySchema


@app.route("/jinja")
def jinja():
    """List companies

    List the x biggest companies
    """
    ibovespa = YahooApi("^BVSP").get_price()
    companies = [
        {"nome": "VALE", "codigo": "VALE3", "peso": "9,71%"},
        {"nome": "BRADESCO", "codigo": "BBDC4", "peso": "8,52%"},
        {"nome": "PETROBRAS", "codigo": "PETR4", "peso": "6,95%"},
        {"nome": "B3", "codigo": "B3SA3", "peso": "4,83%"},
        {"nome": "PETROBRAS", "codigo": "PETR3", "peso": "4,76%"},
        {"nome": "AMBEV S/A", "codigo": "ABEV3", "peso": "4,60%"},
        {"nome": "BANCO DO BRASIL", "codigo": "BBAS3", "peso": "4,05%"},
        {"nome": "ITAUSA", "codigo": "ITSA4", "peso": "3,43%"},
        {"nome": "JBS", "codigo": "JBSS3", "peso": "2,24%"},
        {"nome": "LOJAS RENNER", "codigo": "LREN3", "peso": "2,15%"},
    ]
    return render_template("index.html", companies=companies, ibovespa=ibovespa)


@app.route("/")
def index():
    return db.engine.url.database


@app.route("/companies", methods=["GET"])
@jwt_required
def CompanyAll():
    rowsPerPage = request.args.get(
        "ROWS_PER_PAGE", app.config["ROWS_PER_PAGE"], type=int
    )
    page = request.args.get("page", 1, type=int)
    idFilter = request.args.get("id", None)
    nameFilter = request.args.get("name", None)
    symbolFilter = request.args.get("symbol", None)
    pesoFilter = request.args.get("peso", None)

    user = get_jwt_identity()
    print(user)
    allowed_companies = [
        i.company_id
        for i in UserCompanyPrivilege.query.filter(
            UserCompanyPrivilege.user_id == user
        ).all()
    ]
    print(allowed_companies)
    query = Company.query.filter(Company.id.in_(allowed_companies)).order_by(
        Company.peso.desc()
    )

    if idFilter != None:
        query = query.filter(Company.id == idFilter)

    if nameFilter != None:
        query = query.filter(Company.name == nameFilter)

    if symbolFilter != None:
        query = query.filter(Company.symbol == symbolFilter)

    if pesoFilter != None:
        query = query.filter(Company.peso == pesoFilter)

    pagination = query.paginate(page=page, per_page=rowsPerPage, error_out=False)
    companys = pagination.items
    output = {
        "pagination": {
            "pages_count": pagination.pages,
            "itens_count": pagination.total,
            "itens_per_page": rowsPerPage,
            "prev": pagination.prev_num,
            "next": pagination.next_num,
            "current": pagination.page,
        },
        "itens": [],
        "has_error": False,
    }

    for company in companys:
        data = {}

        data["id"] = company.id
        data["name"] = company.name
        data["symbol"] = company.symbol
        data["peso"] = company.peso
        output["itens"].append(data)

    return jsonify(output)


# -------------------------
# View
# -------------------------


@app.route("/company/<company_id>", methods=["GET"])
@jwt_required
def CompanyView(company_id):
    user = get_jwt_identity()
    allowed_companies = [
        i.company_id
        for i in UserCompanyPrivilege.query.filter(
            UserCompanyPrivilege.user_id == user
        ).all()
    ]
    if int(company_id) in allowed_companies:
        company = Company.query.get(company_id)
    else:
        company = None

    if not company:
        return jsonify(
            {
                "message": Messages.REGISTER_NOT_FOUND.format(company_id),
                "has_error": True,
            }
        )

    data = {"has_error": False}
    data["id"] = company.id
    data["name"] = company.name
    data["symbol"] = company.symbol
    data["peso"] = company.peso

    return jsonify(data)


@app.route("/company/<symbol>/history", methods=["GET"])
@jwt_required
def CompanyHistory(symbol):
    cursor = request.args.get("cursor", None, type=str)

    user = get_jwt_identity()
    allowed_companies = [
        i.company_id
        for i in UserCompanyPrivilege.query.filter(
            UserCompanyPrivilege.user_id == user
        ).all()
    ]

    company = Company.query.filter(
        Company.symbol == symbol and Company.id.in_(allowed_companies)
    ).first()

    if not company:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(symbol), "has_error": True}
        )

    company_id = company.id
    company_symbol = company.symbol

    data = {"has_error": False}
    data["id"] = company.id
    data["name"] = company.name
    data["symbol"] = company.symbol
    data["peso"] = company.peso

    most_recent_quote = (
        Quote.query.filter(Quote.company_id == company_id)
        .order_by(Quote.date.desc())
        .first()
    )

    if not most_recent_quote:
        try:
            stock_data = YahooApi(company.symbol).ticker.history(
                period="1mo", interval="5m"
            )
            TimeSeries(stock_data, company.symbol).insert()
            company.populated = True
        except Exception:
            traceback.print_exc()
            return jsonify(
                {"message": Messages.COULD_NOT_POPULATE_DATA, "has_error": True}
            )
    else:
        if not most_recent_quote.date > datetime.now() - timedelta(minutes=10):
            stock_data = YahooApi(company.symbol).ticker.history(
                start=most_recent_quote.date, interval="5m"
            )
            TimeSeries(stock_data, company.symbol).insert(start=most_recent_quote.date)

    quotes_query = Quote.query.filter(Quote.company_id == company_id)
    if cursor is not None:
        quotes_query.filter(Quote.date > cursor)
    quotes = [quote.dict() for quote in quotes_query.all()]

    data["history"] = quotes

    return jsonify(data)


# -------------------------
# Edit
# -------------------------


@app.route("/company/<company_id>", methods=["PUT"])
@jwt_required
def CompanyEdit(company_id):
    user = get_jwt_identity()

    allowed_companies = [
        i.company_id
        for i in UserCompanyPrivilege.query.filter(
            UserCompanyPrivilege.user_id == user
        ).all()
    ]
    if int(company_id) in allowed_companies:
        company = Company.query.get(company_id)
    else:
        company = None

    if not company:
        return jsonify(
            {
                "message": Messages.REGISTER_NOT_FOUND.format(company_id),
                "has_error": True,
            }
        )

    data = request.get_json()
    errors = CompanySchema().validate(data)

    if errors:
        return (
            jsonify(
                {
                    "message": Messages.FORM_VALIDATION_ERROR,
                    "has_error": True,
                    "errors": errors,
                }
            ),
            200,
        )
    company.name = data["name"]
    company.symbol = data["symbol"]
    company.peso = data["peso"]

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_UPDATED.format("Company"),
                "has_error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "has_error": True}
        )


# -------------------------
# Add
# -------------------------


@app.route("/company", methods=["POST"])
@jwt_required
def CompanyAdd():
    data = request.get_json()
    errors = CompanySchema().validate(data)

    if errors:
        return (
            jsonify(
                {
                    "message": Messages.FORM_VALIDATION_ERROR,
                    "has_error": True,
                    "errors": errors,
                }
            ),
            200,
        )

    company = Company(name=data["name"], symbol=data["symbol"], peso=data["peso"])

    db.session.add(company)
    db.session.flush()
    user = get_jwt_identity()
    db.session.add(UserCompanyPrivilege(user, company.id))

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format("Company"),
                "has_error": False,
            }
        )
    except exc.IntegrityError:
        traceback.print_exc()
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "has_error": True}
        )


# -------------------------
# Delete
# -------------------------


@app.route("/company/<company_id>", methods=["DELETE"])
def CompanyDelete(company_id):

    UserCompanyPrivilege.query.filter(
        UserCompanyPrivilege.company_id == company_id
    ).delete()

    company = Company.query.get(company_id)

    if not company:
        return jsonify(
            {
                "message": Messages.REGISTER_NOT_FOUND.format(company_id),
                "has_error": True,
            }
        )

    db.session.delete(company)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_DELETED.format("Company"),
                "has_error": False,
            }
        )
    except exc.IntegrityError:
        traceback.print_exc()
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "has_error": True}
        )
