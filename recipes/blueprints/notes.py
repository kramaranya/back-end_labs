from flask.views import MethodView
from flask import request, jsonify
from flask_smorest import Blueprint
from recipes.data import NOTES, CATEGORIES, USERS
import datetime

blp = Blueprint("notes", __name__)


def verification(key, value, arr):
    for i in arr:
        if i[key] == value:
            return True
    return False


@blp.route("/notes")
class GetNote(MethodView):
    def get(self):
        return jsonify({"notes": NOTES})


@blp.route("/note")
class PostNote(MethodView):
    def post(self):
        info = request.get_json()

        try:
            if not (verification("id", request.get_json()["user_id"], USERS)
                    and verification("id", request.get_json()["category_id"], CATEGORIES)):
                return "No such user or category"

            info["id"] = request.get_json()["id"]
            info["date"] = datetime.datetime.now()
            info["price"] = request.get_json()["price"]
        except:
            return 'Error while creating new note.'

        NOTES.append(info)
        return info


@blp.get('/notes/<int:user_id>/<int:category_id>')
def get_users_notes_for_categories(user_id, category_id):
    notes = []
    for note in NOTES:
        if note['user_id'] == int(user_id) and note['category_id'] == int(category_id):
            notes.append(note)
    return jsonify({"user": user_id, "category": category_id, "notes": notes})


@blp.route("/notes/<int:user_id>")
def get_users_notes(user_id):
    notes = []
    for note in NOTES:
        if note['user_id'] == int(user_id):
            notes.append(note)
    return jsonify({"user": user_id, "notes": notes})
