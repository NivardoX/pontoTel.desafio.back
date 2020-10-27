from app import db


class Controller(db.Model):
    __tablename__ = "controllers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    resources = db.relationship("Resource", backref="controllers", lazy=True)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, name):
        self.name = name

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Controller %r>" % self.name
