from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_script import Manager
from flask_restplus import Api

app = Flask(__name__)
api = Api(app=app)
CORS(app, resources={"*": {"origins": "*"}})
app.config.from_object("config")
jwt = JWTManager(app)

manager = Manager(app)

name_space = api.namespace("main", description="Main APIs")

# ---------IMPORTS--------------#
