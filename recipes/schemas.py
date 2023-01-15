from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True)

class UserLogin(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    user_id = fields.Int(required=True)
    is_private = fields.Bool(required=True)


class NoteQuerySchema(Schema):
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)


class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    price = fields.Float(required=True)
    date = fields.DateTime("%d-%m-%Y %H:%M", required=False)
