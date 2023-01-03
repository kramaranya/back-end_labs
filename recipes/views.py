from recipes import app
from recipes import data
from flask import jsonify, request
import datetime

@app.route("/")
def default_page():
    return "Welcome to the main page."


'''@app.route("/categories")
def get_categories():
    return jsonify({"categories": data.CATEGORIES})'''


'''@app.route("/users")
def get_users():
    return jsonify({"users": data.USERS})'''


@app.route("/notes")
def get_notes():
    return jsonify({"notes": data.NOTES})


@app.route("/notes/<int:user_id>")
def get_users_notes(user_id):
    notes = []
    for note in data.NOTES:
        if note['user_id'] == int(user_id):
            notes.append(note)
    return jsonify({"user": user_id, "notes": notes})


@app.get('/notes/<int:user_id>/<int:category_id>')
def get_users_notes_for_categories(user_id, category_id):
    notes = []
    for note in data.NOTES:
        if note['user_id'] == int(user_id) and note['category_id'] == int(category_id):
            notes.append(note)
    return jsonify({"user": user_id, "category": category_id, "notes": notes})


'''@app.route("/user", methods=["POST"])
def create_user():
    info = {}
    try:
        info["name"] = request.get_json()["name"]
        info["id"] = request.get_json()["id"]
        if verification("id", request.get_json()["id"], data.USERS):
            return "This user id is already exist."
    except:
        return 'Error while creating new user'
    data.USERS.append(info)
    return info'''


'''@app.route("/category", methods=["POST"])
def create_category():
    info = {}
    try:
        info["title"] = request.get_json()["title"]
        info["id"] = request.get_json()["id"]
        if verification("id", request.get_json()["id"], data.CATEGORIES):
            return "This category id is already exist."
    except:
        return 'Error while creating new category.'
    data.CATEGORIES.append(info)
    return info'''


@app.route("/note", methods=["POST"])
def create_note():
    info = request.get_json()

    try:
        if not (verification("id", request.get_json()["user_id"], data.USERS)
                and verification("id", request.get_json()["category_id"], data.CATEGORIES)):
            return "No such user or category"

        info["id"] = request.get_json()["id"]
        info["date"] = datetime.datetime.now()
        info["price"] = request.get_json()["price"]
    except:
        return 'Error while creating new note.'

    data.NOTES.append(info)
    return info


def verification(key, value, arr):
    for i in arr:
        if i[key] == value:
            return True
    return False
