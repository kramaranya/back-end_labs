from flask.views import MethodView
from flask import request, jsonify
from flask_smorest import Blueprint
from recipes.data import USERS


blp = Blueprint("users", __name__)


def verification(key, value, arr):
    for i in arr:
        if i[key] == value:
            return True
    return False


@blp.route("/users")
class GetUser(MethodView):
    def get(self):
        return jsonify({"users": USERS})


@blp.route("/user")
class PostUser(MethodView):
    def post(self):
        info = {}
        try:
            info["name"] = request.get_json()["name"]
            info["id"] = request.get_json()["id"]
            if verification("id", request.get_json()["id"], USERS):
                return "This user id is already exist."
        except:
            return 'Error while creating new user'
        USERS.append(info)
        return info
