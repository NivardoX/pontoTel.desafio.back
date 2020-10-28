from flask import request, jsonify
from sqlalchemy import exc

import Messages
from app import app, db
from app.models.roles_table import Role
from app.schemas.roles_schema import RolesSchema


@app.route("/roles", methods=["GET"])
def get_roles():
    rowsPerPage = request.args.get(
        "rows_per_page", app.config["ROWS_PER_PAGE"], type=int
    )
    page = request.args.get("page", 1, type=int)
    idFilter = request.args.get("id", None)
    nameFilter = request.args.get("name", None)

    query = Role.query.order_by(Role.id)

    if idFilter is not None:
        query = query.filter(Role.id == idFilter)

    if idFilter is not None:
        query = query.filter(Role.name == nameFilter)

    pagination = query.paginate(page=page, per_page=rowsPerPage, error_out=False)
    roless = pagination.items
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

    for roles in roless:
        output["itens"].append({"id": roles.id, "nome": roles.name})

    return jsonify(output)


@app.route("/roles", methods=["POST"])
def post_roles():

    data = request.get_json()
    data, errors = RolesSchema().load(data)

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

    roles = Role(name=data["name"])

    db.session.add(roles)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format("Roles"),
                "has_error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "has_error": True}
        )


@app.route("/roles", methods=["PATCH"])
def patch_roles(id):

    roles = Role.query.get(id)

    if not roles:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(id), "has_error": True}
        )

    data = request.get_json()
    data, errors = RolesSchema().load(data)

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

    roles.nome = data["nome"]

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_UPDATED.format("Roles"),
                "has_error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "has_error": True}
        )


@app.route("/role/<id>", methods=["GET"])
def get_role(id):

    roles = Role.query.get(id)

    if not roles:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(id), "has_error": True}
        )

    data = {"id": roles.id, "name": roles.name, "has_error": False}
    return jsonify(data)


@app.route("/roles/<id>", methods=["DELETE"])
def delete_role(self, id):

    roles = Role.query.get(id)

    if not roles:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(id), "has_error": True}
        )

    db.session.delete(roles)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_DELETED.format("Roles"),
                "has_error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "has_error": True}
        )
