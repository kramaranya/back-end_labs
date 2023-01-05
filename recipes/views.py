from recipes import app
from flask_smorest import Api
from recipes.db import db

from recipes.blueprints.user import blp as UserBlueprint
from recipes.blueprints.category import blp as CategoryBlueprint
from recipes.blueprints.note import blp as NoteBlueprint


app.config["PROPAGATE_EXCEPTION"] = True
app.config["API_TITLE"] = "Backend labs Kramar"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

db.init_app(app)

with app.app_context():
    db.create_all()

api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(NoteBlueprint)


@app.route("/")
def default_page():
    return "Welcome to the main page."
