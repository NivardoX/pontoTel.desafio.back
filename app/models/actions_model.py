from app import db


class Action(db.Model):
    __tablename__ = "actions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    resources = db.relationship("Resource", backref="actions", lazy=True)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, name):
        self.name = name

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Action %r>" % self.name
