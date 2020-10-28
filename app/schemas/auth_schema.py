from marshmallow import Schema, fields, INCLUDE


class AuthSchema(Schema):
    class Meta:
        unknown = INCLUDE
    username = fields.Str(required=True)
    password = fields.Str(required=True)
