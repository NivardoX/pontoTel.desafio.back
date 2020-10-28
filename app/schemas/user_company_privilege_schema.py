from marshmallow import Schema, fields, INCLUDE


class UserCompanyPrivilegeSchema(Schema):
    class Meta:
        unknown = INCLUDE
    user_id = fields.Integer(required=True)
    company_id = fields.Integer(required=True)
