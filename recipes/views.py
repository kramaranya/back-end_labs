from recipes import app
from recipes import data
from flask import jsonify, request
import datetime

from flask_smorest import Blueprint as blp
from flask_smorest import Api
from recipes.data import *

from recipes.blueprints.users import blp as UserBlueprint
from recipes.blueprints.categories import blp as CategoryBlueprint
from recipes.blueprints.notes import blp as NoteBlueprint

app.config["PROPAGATE_EXCEPTION"] = True
app.config["API_TITLE"] = "Backend labs Kranar"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(NoteBlueprint)


@app.route("/")
def default_page():
    return "Welcome to the main page."
