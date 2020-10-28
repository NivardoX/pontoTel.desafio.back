from quart_openapi import Resource

from app import app, db, Messages
from flask import request, jsonify
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
)

from app import User
from werkzeug.security import check_password_hash


# --------------------------------------------------------------------------------------------------#
from app.schemas.auth_schema import AuthSchema


@app.route("/auth", methods=["POST"])
def login():
    data = request.get_json()
    errors = AuthSchema().validate(data)

    if errors:
        return (
            jsonify(
                {
                    "message": Messages.FORM_VALIDATION_ERROR,
                    "errors": errors,
                    "has_error": True,
                }
            ),
            200,
        )
    user = User.query.filter(User.username == data["username"]).first()

    pusername = data["username"]
    ppassword = data["password"]

    # verify if the username exists in database
    user = User.query.filter(User.username == pusername).first()

    if not user:
        return (
            jsonify({"message": Messages.AUTH_USER_NOT_FOUND, "has_error": True}),
            200,
        )
    elif not check_password_hash(user.password, ppassword):
        return (
            jsonify({"message": Messages.AUTH_USER_PASS_ERROR, "has_error": True}),
            200,
        )

    return (
        jsonify(
            {
                "access_token": create_access_token(identity=user.id),
                "refresh_token": create_refresh_token(identity=user.id),
                "user_role": user.role_id,
                "has_error": False,
            }
        ),
        200,
    )


# --------------------------------------------------------------------------------------------------#


@app.route("/refresh", methods=["POST"])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()

    return jsonify({"access_token": create_access_token(identity=current_user)}), 200

@app.route("/me", methods=["GET"])
@jwt_required
def me():
    current_user = get_jwt_identity()
    print(current_user)
    user = User.query.get(current_user)
    return (
        jsonify(
            {
                "username": user.username,
                "email": user.email,
                "role_id": user.role_id,
                "role": {"id": user.roles.id, "name": user.roles.name},
            }
        ),
        200,
    )


# --------------------------------------------------------------------------------------------------#
