from marshmallow import Schema, fields, INCLUDE


class StockSchema(Schema):
    class Meta:
        unknown = INCLUDE
    symbol = fields.String(required=True)
