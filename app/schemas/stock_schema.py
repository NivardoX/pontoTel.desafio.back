from marshmallow import Schema, fields


class StockSchema(Schema):
    symbol = fields.String(required=True)
