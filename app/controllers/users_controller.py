from pprint import pprint

from app import app, db, Messages, User
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy import exc
from werkzeug.security import generate_password_hash

from app.components.wrappers.resource import resource


@app.route("/user/all", methods=["GET"])
@jwt_required
@resource("users-all")
def userAll():

    page = request.args.get("page", 1, type=int)
    usernameFilter = request.args.get("username", None)
    rowsPerPage = app.config["ROWS_PER_PAGE"]
    query = User.query.order_by(User.username)

    if usernameFilter != None:
        query = query.filter(User.username.ilike("%%{}%%".format(usernameFilter)))

    pagination = query.paginate(page=page, per_page=rowsPerPage, error_out=False)
    users = pagination.items
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

    for user in users:
        data = {}
        data["id"] = user.id
        data["username"] = user.username
        data["email"] = user.email
        data["role_id"] = user.role_id
        data["role"] = {}
        data["role"]["id"] = user.roles.id
        data["role"]["name"] = user.roles.name
        data["role_nome"] = user.roles.name

        if data["role_id"] == 3 and user.professor_id != None:
            data["professor_id"] = user.professor_id
            data["professor_nome"] = user.professor.nome

        output["itens"].append(data)

    return jsonify(output)


# --------------------------------------------------------------------------------------------------#


@app.route("/user/view/<user_id>", methods=["GET"])
@jwt_required
@resource("users-view")
def userView(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(user_id), "error": True}
        )

    data = {"error": False}
    data["id"] = user.id
    data["username"] = user.username
    data["email"] = user.email
    data["role_id"] = user.role_id
    data["role"] = {}
    data["role"]["id"] = user.roles.id
    data["role"]["name"] = user.roles.name
    data["role_nome"] = user.roles.name
    if data["role_id"] == 3 and user.professor_id != None:
        data["professor_id"] = user.professor_id
        data["professor_nome"] = user.professor.nome
    return jsonify(data)


# --------------------------------------------------------------------------------------------------#


@app.route("/user/add", methods=["POST"])
@jwt_required
@resource("users-add")
def userAdd():
    data = request.get_json()
    validator = UserValidator(data)
    validator.addPasswordField()

    errors = validator.validate()

    if errors["has"]:
        return (
            jsonify(
                {
                    "message": Messages.FORM_VALIDATION_ERROR,
                    "error": errors["has"],
                    "errors": errors,
                }
            ),
            200,
        )

    errors = validator.validateUsername()

    if errors["has"]:
        return (
            jsonify(
                {
                    "message": Messages.FORM_VALIDATION_ERROR,
                    "error": errors["has"],
                    "errors": errors,
                }
            ),
            200,
        )

    hashed_pass = generate_password_hash(data["password"], method="sha256")
    user = User(
        username=data["username"],
        password=hashed_pass,
        role_id=data["role_id"],
        professor_id=data["professor_id"] if "professor_id" in data else None,
        email=data["email"],
    )

    db.session.add(user)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format("Usuário"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CREATE_INTEGRITY_ERROR, "error": True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/user/edit/<user_id>", methods=["PUT"])
@jwt_required
@resource("users-edit")
def userEdit(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(user_id), "error": True}
        )

    data = request.get_json()
    validator = UserValidator(data)
    errors = validator.validate()

    if errors["has"]:
        return (
            jsonify(
                {
                    "message": Messages.FORM_VALIDATION_ERROR,
                    "error": errors["has"],
                    "errors": errors,
                }
            ),
            200,
        )

    user.username = data["username"]
    user.email = data["email"]
    user.role_id = data["role_id"]

    if data["role_id"] == "3" or data["role_id"] == 3:
        user.professor_id = data["professor_id"]
    else:
        user.professor_id = None

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_UPDATED.format("Usuário"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "error": True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/user/delete/<user_id>", methods=["DELETE"])
@jwt_required
@resource("users-delete")
def userDelete(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(user_id), "error": True}
        )

    db.session.delete(user)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_DELETED.format("Usuário"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        return jsonify(
            {"message": Messages.REGISTER_DELETE_INTEGRITY_ERROR, "error": True}
        )
