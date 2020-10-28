from app import db, Messages
from quart import jsonify
from functools import wraps
from flask_jwt_extended import get_jwt_identity

from app import User
from app import Role
from app import Resource
from app import Privilege
from app import Action
from app import Controller
from typing import Callable


def resource(resource_name: str) -> Callable:
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            user = User.query.get(get_jwt_identity())
            user_role = user.role_id
            contr, act = resource_name.split("-")

            data = (
                db.session.query(
                    Privilege.allow,
                    Privilege.role_id,
                    Controller.name.label("contr"),
                    Action.name.label("act"),
                )
                .join(Resource, Privilege.resource_id == Resource.id)
                .join(Action, Resource.action_id == Action.id)
                .join(Controller, Resource.controller_id == Controller.id)
                .filter(
                    Privilege.role_id == user_role,
                    Controller.name == contr,
                    Action.name == act,
                )
                .first()
            )

            if data == None:
                return (
                    jsonify(
                        {
                            "description": Messages.AUTH_USER_DENIED,
                            "error": "Unauthorized Access",
                            "status_code": 401,
                        }
                    ),
                    401,
                )

            if not data.allow:
                return (
                    jsonify(
                        {
                            "description": Messages.AUTH_USER_DENIED,
                            "error": "Unauthorized Access",
                            "status_code": 401,
                        }
                    ),
                    401,
                )

            return f(*args, **kwargs)

        return wrapped

    return wrapper
