import sys

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy import true

from recipes.schemas import NoteSchema
from recipes.models.note import NoteModel
from recipes.models.category import CategoryModel
from recipes.models.user import UserModel
from recipes.schemas import NoteQuerySchema
from recipes.db import db
from sqlalchemy.exc import IntegrityError, NoResultFound

blp = Blueprint("notes", __name__, description="Operations on notes")


@blp.route("/note/<string:note_id>")
class Note(MethodView):
    @blp.response(200, NoteSchema)
    def get(self, note_id):
        return NoteModel.query.get_or_404(note_id)


@blp.route("/notes")
class NotesList(MethodView):
    @blp.arguments(NoteQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, NoteSchema(many=True))
    def get(self, **kwargs):
        user_id = kwargs.get("user_id")

        if not user_id:
            abort(400, "Bad request: Username needed")

        query = NoteModel.query.filter(NoteModel.user_id == user_id)

        category_id = kwargs.get("category_id")

        if category_id:
            query = query.filter(NoteModel.category_id == category_id)

        return query.all()


@blp.route("/note")
class NoteList(MethodView):
    @blp.response(200, NoteSchema(many=True))
    def get(self):
        return NoteModel.query.all()

    @blp.arguments(NoteSchema)
    @blp.response(200, NoteSchema)
    def post(self, note_data):
        note = NoteModel(**note_data)
        user_id = note_data.get("user_id")
        category_id = note_data.get("category_id")

        try:
            category = CategoryModel.query.filter(CategoryModel.id == category_id).one()
            user = UserModel.query.filter(UserModel.id == user_id).one()
            print(category.is_private, file=sys.stderr)
            if category.is_private and category.user_id != user_id:
                abort(404, message="Category is private")
            db.session.add(category)
            db.session.add(user)
            db.session.add(note)
            db.session.commit()
        except NoResultFound:
            abort(404, message="Data not found")
        except IntegrityError:
            abort(400, message="Something went wrong")

        return note
