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
manager.add_command('db', MigrateCommand)

# --MODELS-- #
from app.models.actions_model import *
from app.models.privileges_table import *
from app.models.resources_table import *
from app.models.users_table import *
from app.models.roles_table import *
from app.models.controllers_model import *

# --CONTROLLERS-- #

from app.controllers import company_controller
from app.controllers import stock_quote_controller
from app.controllers import users_controller
from app.controllers import auth_controller
from app.controllers.queue_controller import *


