from flask.views import MethodView
from flask import request, jsonify
from flask_smorest import Blueprint, abort
from recipes.data import NOTES, CATEGORIES, USERS
from recipes.schemas import NoteSchema
import datetime

blp = Blueprint("notes", __name__, description="Operations on notes")


def verification(key, value, arr):
    for i in arr:
        if i[key] == value:
            return True
    return False


@blp.route("/notes")
class GetNote(MethodView):
    @blp.response(200, NoteSchema(many=True))
    def get(self):
        return jsonify({"notes": NOTES})


@blp.route("/note")
class PostNote(MethodView):
    @blp.arguments(NoteSchema)
    @blp.response(200, NoteSchema)
    def post(self, note_data):
        if not (verification("id", note_data["user_id"], USERS)
                and verification("id", note_data["category_id"], CATEGORIES)) or \
                verification("id", note_data["id"], NOTES):
            abort(400, message="No such user or category or note id is already exist")
        note_data["date"] = datetime.datetime.now()
        NOTES.append(note_data)
        return note_data


@blp.route('/notes/<int:user_id>/<int:category_id>')
@blp.response(200, NoteSchema(many=True))
def get_users_notes_for_categories(user_id, category_id):
    notes = []
    for note in NOTES:
        if note['user_id'] == int(user_id) and note['category_id'] == int(category_id):
            notes.append(note)
    return jsonify({"user": user_id, "category": category_id, "notes": notes})


@blp.route("/notes/<int:user_id>")
@blp.response(200, NoteSchema(many=True))
def get_users_notes(user_id):
    notes = []
    for note in NOTES:
        if note['user_id'] == int(user_id):
            notes.append(note)
    return jsonify({"user": user_id, "notes": notes})