from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required
from flask_smorest import Blueprint, abort
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from recipes.schemas import UserSchema, UserLogin
from recipes.models.user import UserModel
from recipes.db import db
from sqlalchemy.exc import IntegrityError

blp = Blueprint("users", __name__, description="Operations on users")


@blp.route("/user/<string:username>")
class User(MethodView):
    @blp.response(200, UserSchema)
    @jwt_required()
    def get(self, user_id):
        return UserModel.query.get_or_404(user_id)


@blp.route("/register")
class UserRegister(MethodView):
    @blp.response(200, UserSchema(many=True))
    @jwt_required()
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        user = UserModel(name=user_data["name"],
                         password=pbkdf2_sha256.hash(user_data["password"]))

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="This username is already used")

        return user


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserLogin)
    @blp.response(200, UserLogin)
    def post(self, user_data):
        user = UserModel.query.filter_by(name=user_data["username"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id)
            return jsonify({"status": "Ok", "access_token": access_token})

        return abort(400, message="User not found")