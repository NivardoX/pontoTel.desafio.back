from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_script import Manager


app = Flask(__name__)
CORS(app, resources={"*": {"origins": "*"}})
app.config.from_object('config')
jwt = JWTManager(app)

manager = Manager(app)
