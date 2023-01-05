from flask.views import MethodView
from flask_smorest import Blueprint, abort
from recipes.schemas import UserSchema
from recipes.models.user import UserModel
from recipes.db import db
from sqlalchemy.exc import IntegrityError

blp = Blueprint("users", __name__, description="Operations on users")


@blp.route("/user/<string:username>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        return UserModel.query.get_or_404(user_id)

    @blp.response(200, UserSchema)
    def delete(self, user_id):
        raise NotImplementedError("Not implemented now")


@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="This username is already used")

        return user
