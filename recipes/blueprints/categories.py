from flask.views import MethodView
from flask import request, jsonify
from flask_smorest import Blueprint
from recipes.data import CATEGORIES
from recipes.schemas import CategorySchema

blp = Blueprint("categories", __name__)


def verification(key, value, arr):
    for i in arr:
        if i[key] == value:
            return True
    return False


@blp.route("/categories")
class GetCategory(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return jsonify({"categories": CATEGORIES})


@blp.route("/category")
class PostCategory(MethodView):
    @blp.arguments(CategorySchema)
    def post(self, category_data):
        if verification("id", category_data["id"], CATEGORIES):
            return "This category id is already exist."
        CATEGORIES.append(category_data)
        return category_data
