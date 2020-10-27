from marshmallow import Schema, fields


class CompanySchema(Schema):
    name = fields.Str(required=True)
    symbol = fields.Str(required=True)
    peso = fields.Float()
