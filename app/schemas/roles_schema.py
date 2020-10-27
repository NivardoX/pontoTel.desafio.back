from marshmallow import Schema,fields


class RolesSchema(Schema):
    name = fields.Str(required=True)

