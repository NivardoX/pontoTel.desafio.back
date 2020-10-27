from flask import render_template, request, jsonify
from sqlalchemy import exc

import Messages
from app import app, db
from app.components.yahooApi import YahooApi
from app.models.companies_model import Company as company, Company
from app.schemas.company_schema import CompanySchema


@app.route("/")
def index():
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
    return render_template(
        "index.html", companies=companies, ibovespa=ibovespa
    )


@app.route('/companies', methods=['GET'])
def CompanyAll():
    rowsPerPage = request.args.get('rows_per_page', app.config['ROWS_PER_PAGE'], type=int)
    page = request.args.get('page', 1, type=int)
    idFilter = request.args.get('id', None)
    nameFilter = request.args.get('name', None)
    symbolFilter = request.args.get('symbol', None)
    pesoFilter = request.args.get('peso', None)

    query = Company.query.order_by(Company.peso.desc())

    if (idFilter != None):
        query = query.filter(
            Company.id == idFilter)

    if (nameFilter != None):
        query = query.filter(
            Company.name == nameFilter)

    if (symbolFilter != None):
        query = query.filter(
            Company.symbol == symbolFilter)

    if (pesoFilter != None):
        query = query.filter(
            Company.peso == pesoFilter)

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
        "error": False,
    }

    for company in companys:
        data = {}

        data['id'] = company.id
        data['name'] = company.name
        data['symbol'] = company.symbol
        data['peso'] = company.peso
        output["itens"].append(data)

    return jsonify(output)


# -------------------------
# View
# -------------------------


@app.route('/company/<company_id>', methods=['GET'])
def CompanyView(company_id):
    company = Company.query.get(company_id)

    if not company:
        return jsonify({'message': Messages.REGISTER_NOT_FOUND.format(company_id), 'has_error': True})

    data = {'has_error': False}
    data['id'] = company.id
    data['name'] = company.name
    data['symbol'] = company.symbol
    data['peso'] = company.peso

    return jsonify(data)


@app.route('/company/<symbol>/history', methods=['GET'])
def CompanyHistory(symbol):
    company = db.session.query(Company).filter(Company.symbol==symbol).first()

    if not company:
        return jsonify({'message': Messages.REGISTER_NOT_FOUND.format(symbol), 'has_error': True})

    data = {'has_error': False}
    data['id'] = company.id
    data['name'] = company.name
    data['symbol'] = company.symbol
    data['peso'] = company.peso
    data['history'] = YahooApi(company.symbol).get_history(period="1d").values.tolist()

    return jsonify(data)


# -------------------------
# Edit
# -------------------------


@app.route('/company/<company_id>', methods=['PATCH'])
def CompanyEdit(company_id):
    company = Company.query.get(company_id)

    if not company:
        return jsonify({'message': Messages.REGISTER_NOT_FOUND.format(company_id), 'has_error': True})

    data = request.get_json()
    errors = CompanySchema().validate(data)

    if errors:
        return jsonify({'message': Messages.FORM_VALIDATION_ERROR, 'has_error':True, 'errors': errors}), 200
    company.name = data['name']
    company.symbol = data['symbol']
    company.peso = data['peso']

    try:
        db.session.commit()
        return jsonify({'message': Messages.REGISTER_SUCCESS_UPDATED.format("Company"), 'has_error': False})
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({'message': Messages.REGISTER_CHANGE_INTEGRITY_ERROR, 'has_error': True})


# -------------------------
# Add
# -------------------------



@app.route('/company', methods=['POST'])
def CompanyAdd():
    data = request.get_json()
    errors = CompanySchema().validate(data)

    if errors:
        return jsonify({'message': Messages.FORM_VALIDATION_ERROR, 'has_error':True, 'errors': errors}), 200

    company = Company(
        name=data['name'],
        symbol=data['symbol'],
        peso=data['peso']
    )

    db.session.add(company)

    try:
        db.session.commit()
        return jsonify({'message': Messages.REGISTER_SUCCESS_CREATED.format("Company"), 'has_error': False})
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({'message': Messages.REGISTER_CHANGE_INTEGRITY_ERROR, 'has_error': True})


# -------------------------
# Delete
# -------------------------


@app.route('/company/<company_id>', methods=['DELETE'])
def CompanyDelete(company_id):
    company = Company.query.get(company_id)

    if not company:
        return jsonify({'message': Messages.REGISTER_NOT_FOUND.format(company_id), 'has_error': True})

    db.session.delete(company)

    try:
        db.session.commit()
        return jsonify({'message': Messages.REGISTER_SUCCESS_DELETED.format("Company"), 'has_error': False})
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({'message': Messages.REGISTER_CHANGE_INTEGRITY_ERROR, 'has_error': True})
