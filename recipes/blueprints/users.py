from flask.views import MethodView
from flask import request, jsonify
from flask_smorest import Blueprint
from recipes.data import USERS
from recipes.schemas import UserSchema


blp = Blueprint("users", __name__)


def verification(key, value, arr):
    for i in arr:
        if i[key] == value:
            return True
    return False


@blp.route("/users")
class GetUser(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return jsonify({"users": USERS})


@blp.route("/user")
class PostUser(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if verification("id", user_data["id"], USERS):
            return "This user id is already exist."
        USERS.append(user_data)
        return user_data
