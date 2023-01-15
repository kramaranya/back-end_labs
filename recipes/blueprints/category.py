from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort

from recipes.models import UserModel
from recipes.schemas import CategorySchema
from recipes.models.category import CategoryModel
from recipes.db import db
from sqlalchemy.exc import IntegrityError

blp = Blueprint("categories", __name__, description="Operations on categories")


@blp.route("/category/<string:category_title>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        return CategoryModel.query.get_or_404(category_id)


@blp.route("/category")
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    @jwt_required()
    def post(self, category_data):
        category = CategoryModel(**category_data)
        user_id = category_data.get("user_id")

        try:
            user = UserModel.query.filter(UserModel.id == user_id).one()
            db.session.add(category)
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="This category already exists")

        return category
