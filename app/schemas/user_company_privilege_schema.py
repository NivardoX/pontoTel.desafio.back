from marshmallow import Schema, fields


class UserCompanyPrivilegeSchema(Schema):
    user_id = fields.Integer(required=True)
    company_id = fields.Integer(required=True)
