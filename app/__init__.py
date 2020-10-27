import zmq as zmq
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_jwt_extended import JWTManager
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import Messages

app = Flask(__name__)
app.config.from_object("config")
jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)


context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

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
