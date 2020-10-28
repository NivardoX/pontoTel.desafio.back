from marshmallow import Schema, fields, INCLUDE


class CompanySchema(Schema):
    class Meta:
        unknown = INCLUDE
    name = fields.Str(required=True)
    symbol = fields.Str(required=True)
    peso = fields.Float()
