from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)


class NoteSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    date = fields.DateTime("%d-%m-%Y %H:%M", required=False)
    price = fields.Float(required=True)