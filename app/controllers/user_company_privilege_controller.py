from flask import request, jsonify
from itsdangerous import exc

import Messages
from app import UserCompanyPrivilege, app, db
from app.schemas.user_company_privilege_schema import UserCompanyPrivilegeSchema


@app.route("/user-company-privilege/all", methods=["GET"])
def UsercompanyprivilegeAll():
    rowsPerPage = request.args.get(
        "rows_per_page", app.config["ROWS_PER_PAGE"], type=int
    )
    page = request.args.get("page", 1, type=int)
    idFilter = request.args.get("id", None)
    user_idFilter = request.args.get("user_id", None)
    company_idFilter = request.args.get("company_id", None)

    query = UserCompanyPrivilege.query.order_by(UserCompanyPrivilege.id)

    if idFilter != None:
        query = query.filter(UserCompanyPrivilege.id == idFilter)

    if user_idFilter != None:
        query = query.filter(UserCompanyPrivilege.user_id == user_idFilter)

    if company_idFilter != None:
        query = query.filter(UserCompanyPrivilege.company_id == company_idFilter)

    pagination = query.paginate(page=page, per_page=rowsPerPage, error_out=False)
    usercompanyprivileges = pagination.items
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

    for usercompanyprivilege in usercompanyprivileges:
        data = {}

        data["id"] = usercompanyprivilege.id
        data["user_id"] = usercompanyprivilege.user_id
        data["company_id"] = usercompanyprivilege.company_id
        output["itens"].append(data)

    return jsonify(output)


# -------------------------
# View
# -------------------------


@app.route("/user-company-privilege/view/<usercompanyprivilege_id>", methods=["GET"])
def UsercompanyprivilegeView(usercompanyprivilege_id):
    usercompanyprivilege = UserCompanyPrivilege.query.get(usercompanyprivilege_id)

    if not usercompanyprivilege:
        return jsonify(
            {
                "message": Messages.REGISTER_NOT_FOUND.format(usercompanyprivilege_id),
                "has_error": True,
            }
        )

    data = {"has_error": False}
    data["id"] = usercompanyprivilege.id
    data["user_id"] = usercompanyprivilege.user_id
    data["company_id"] = usercompanyprivilege.company_id
    return jsonify(data)


# -------------------------
# Edit
# -------------------------


@app.route("/user-company-privilege/edit/<usercompanyprivilege_id>", methods=["PUT"])
def UsercompanyprivilegeEdit(usercompanyprivilege_id):
    usercompanyprivilege = UserCompanyPrivilege.query.get(usercompanyprivilege_id)

    if not usercompanyprivilege:
        return jsonify(
            {
                "message": Messages.REGISTER_NOT_FOUND.format(usercompanyprivilege_id),
                "has_error": True,
            }
        )

    data = request.get_json()
    errors = UserCompanyPrivilegeSchema.validate(data)

    if errors:
        return (
            jsonify(
                {
                    "message": Messages.FORM_VALIDATION_ERROR,
                    "has_error": errors["has"],
                    "errors": errors,
                }
            ),
            200,
        )
    usercompanyprivilege.user_id = data["user_id"]
    usercompanyprivilege.company_id = data["company_id"]

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_UPDATED.format(
                    "UserCompanyPrivilege"
                ),
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


@app.route("/user-company-privilege/add", methods=["POST"])
def UsercompanyprivilegeAdd():
    data = request.get_json()

    data = request.get_json()
    errors = UserCompanyPrivilegeSchema.validate(data)
    if errors:
        return (
            jsonify(
                {
                    "message": Messages.FORM_VALIDATION_ERROR,
                    "has_error": errors["has"],
                    "errors": errors,
                }
            ),
            200,
        )

    usercompanyprivilege = UserCompanyPrivilege(
        user_id=data["user_id"], company_id=data["company_id"]
    )

    db.session.add(usercompanyprivilege)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format(
                    "UserCompanyPrivilege"
                ),
                "has_error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "has_error": True}
        )


# -------------------------
# Delete
# -------------------------


@app.route(
    "/user-company-privilege/delete/<usercompanyprivilege_id>", methods=["DELETE"]
)
def UsercompanyprivilegeDelete(usercompanyprivilege_id):
    usercompanyprivilege = UserCompanyPrivilege.query.get(usercompanyprivilege_id)

    if not usercompanyprivilege:
        return jsonify(
            {
                "message": Messages.REGISTER_NOT_FOUND.format(usercompanyprivilege_id),
                "has_error": True,
            }
        )

    db.session.delete(usercompanyprivilege)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_DELETED.format(
                    "UserCompanyPrivilege"
                ),
                "has_error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "has_error": True}
        )
