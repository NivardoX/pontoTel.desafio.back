from marshmallow import Schema, fields, INCLUDE


class RolesSchema(Schema):
    class Meta:
        unknown = INCLUDE

    name = fields.Str(required=True)
