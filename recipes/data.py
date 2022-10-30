import datetime


CATEGORIES = [
    {
        "id": 1,
        "title": "English"
    },
    {
        "id": 2,
        "title": "Math"
    },
    {
        "id": 3,
        "title": "Programming"
    },
    {
        "id": 4,
        "title": "Ukrainian"
    }
]

USERS = [
    {
        "id": 1,
        "name": "Anya",
    },
    {
        "id": 2,
        "name": "Yana",
    },
    {
        "id": 3,
        "name": "Sasha",
    }
]

NOTES = [
    {
        "id": 1,
        "user_id": 1,
        "category_id": 3,
        "date": datetime.datetime.now(),
        "price": 550
    },
    {
        "id": 2,
        "user_id": 1,
        "category_id": 4,
        "date": datetime.datetime.now(),
        "price": 485
    },
    {
        "id": 3,
        "user_id": 2,
        "category_id": 2,
        "date": datetime.datetime.now(),
        "price": 390
    },
    {
        "id": 4,
        "user_id": 2,
        "category_id": 1,
        "date": datetime.datetime.now(),
        "price": 118
    },
    {
        "id": 5,
        "user_id": 3,
        "category_id": 3,
        "date": datetime.datetime.now(),
        "price": 120
    }
]