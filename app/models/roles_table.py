from app import db


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    users = db.relationship("User", backref="roles", lazy=True)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, name):
        self.name = name

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Role %r>" % self.name
