from flask.views import MethodView
from flask import request, jsonify
from flask_smorest import Blueprint
from recipes.data import CATEGORIES

blp = Blueprint("categories", __name__)


def verification(key, value, arr):
    for i in arr:
        if i[key] == value:
            return True
    return False


@blp.route("/categories")
class GetCategory(MethodView):
    def get(self):
        return jsonify({"categories": CATEGORIES})


@blp.route("/category")
class PostCategory(MethodView):
    def post(self):
        info = {}
        try:
            info["title"] = request.get_json()["title"]
            info["id"] = request.get_json()["id"]
            if verification("id", request.get_json()["id"], CATEGORIES):
                return "This category id is already exist."
        except:
            return 'Error while creating new category.'
        CATEGORIES.append(info)
        return info
