from app import db


class Resource(db.Model):
    __tablename__ = "resources"

    id = db.Column(db.Integer, primary_key=True)
    action_id = db.Column(db.Integer, db.ForeignKey("actions.id"), nullable=False)
    controller_id = db.Column(
        db.Integer, db.ForeignKey("controllers.id"), nullable=False
    )
    privileges = db.relationship("Privilege", backref="resources", lazy=True)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, action_id, controller_id):
        self.action_id = action_id
        self.controller_id = controller_id

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Resource %d-%d>" % (self.action_id, self.controller_id)
