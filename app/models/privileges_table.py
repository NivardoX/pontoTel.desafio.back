from sqlalchemy import PrimaryKeyConstraint

from app import db


class Privilege(db.Model):
    __tablename__ = "privileges"

    allow = db.Column(db.Boolean, nullable=False)
    role_id = db.Column(
        db.Integer, db.ForeignKey("roles.id"), nullable=False, primary_key=True
    )
    resource_id = db.Column(
        db.Integer, db.ForeignKey("resources.id"), nullable=False, primary_key=True
    )

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, allow, role_id, resource_id):
        self.allow = allow
        self.role_id = role_id
        self.resource_id = resource_id

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Privillege %s-%d-%d>" % (self.allow, self.role_id, self.resource_id)
