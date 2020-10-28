import os

import zmq as zmq
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_jwt_extended import JWTManager
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import Messages
from config import TEST_DB_URL

app = Flask(__name__)
CORS(app, resources={"*": {"origins": "*"}})
app.config.from_object("config")
if os.environ.get("STAGE", None) == "test":
    app.config["SQLALCHEMY_DATABASE_URI"] = TEST_DB_URL

db = SQLAlchemy(app)

jwt = JWTManager(app)
migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command("db", MigrateCommand)


context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.LINGER, 0)
socket.RCVTIMEO = 1000

# --MODELS-- #
from app.models.actions_model import *
from app.models.privileges_table import *
from app.models.resources_table import *
from app.models.users_model import *
from app.models.roles_table import *
from app.models.controllers_model import *
from app.models.quotes_model import *
from app.models.companies_model import *
from app.models.users_companies_privileges_model import *

# --CONTROLLERS-- #

from app.controllers import company_controller
from app.controllers import stock_quote_controller
from app.controllers import users_controller
from app.controllers import auth_controller
from app.controllers import role_controller
from app.controllers import user_company_privilege_controller
