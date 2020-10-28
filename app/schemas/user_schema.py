from marshmallow import Schema, fields, INCLUDE


class UserSchema(Schema):
    class Meta:
        unknown = INCLUDE

    email = fields.Email(required=True)
    role_id = fields.Integer(required=True)
    password = fields.String()
    username = fields.String(required=True)
    nome = fields.String()
