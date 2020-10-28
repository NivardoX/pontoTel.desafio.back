from pprint import pprint

from app import app, db, Messages, User, UserCompanyPrivilege
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy import exc
from werkzeug.security import generate_password_hash

from app.components.wrappers.resource import resource
from app.schemas.user_schema import UserSchema


@app.route("/users", methods=["GET"])
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
        'has_error': False,
    }

    for user in users:
        data = {}
        data["id"] = user.id
        data["username"] = user.username
        data["email"] = user.email
        data["role_id"] = user.role_id
        data["name"] = user.name

        data["role"] = {}
        data["role"]["id"] = user.roles.id
        data["role"]["name"] = user.roles.name
        data["role_nome"] = user.roles.name

        output["itens"].append(data)

    return jsonify(output)


# --------------------------------------------------------------------------------------------------#


@app.route("/user/<user_id>", methods=["GET"])
@jwt_required
@resource("users-view")
def userView(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(user_id), 'has_error': True}
        )

    data = {'has_error': False}
    data["id"] = user.id
    data["username"] = user.username
    data["email"] = user.email
    data["role_id"] = user.role_id
    data["name"] = user.name

    data["role"] = {}
    data["role"]["id"] = user.roles.id
    data["role"]["name"] = user.roles.name
    data["role_nome"] = user.roles.name

    return jsonify(data)


# --------------------------------------------------------------------------------------------------#


@app.route("/user", methods=["POST"])
@jwt_required
@resource("users-add")
def userAdd():
    data = request.get_json()

    errors = UserSchema().validate(data)

    if errors:
        print(errors)
        return (

            jsonify(
                {
                    "message": Messages.FORM_VALIDATION_ERROR,
                    'has_error': True,
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
        email=data["email"],
        name=data['name']
    )
    db.session.add(user)
    db.session.flush()
    user_ibov_privilege = UserCompanyPrivilege(user.id,67)
    db.session.add(user_ibov_privilege)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format("Usuário"),
                'has_error': False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CREATE_INTEGRITY_ERROR, 'has_error': True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/user/<user_id>", methods=["PUT"])
@jwt_required
@resource("users-edit")
def userEdit(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(user_id), 'has_error': True}
        )

    data = request.get_json()
    errors = UserSchema().validate(data)


    if errors:
        return (
            jsonify(
                {
                    "message": Messages.FORM_VALIDATION_ERROR,
                    'has_error': True,
                    "errors": errors,
                }
            ),
            200,
        )

    user.username = data["username"]
    user.name = data["name"]
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
                'has_error': False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, 'has_error': True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/user/<user_id>", methods=["DELETE"])
@jwt_required
@resource("users-delete")
def userDelete(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(user_id), 'has_error': True}
        )

    UserCompanyPrivilege.query.filter(UserCompanyPrivilege.user_id==user_id).delete()
    db.session.delete(user)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_DELETED.format("Usuário"),
                'has_error': False,
            }
        )
    except exc.IntegrityError:
        return jsonify(
            {"message": Messages.REGISTER_DELETE_INTEGRITY_ERROR, 'has_error': True}
        )
