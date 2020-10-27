from app import db


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    symbol = db.Column(db.String(255), unique=True, nullable=False)
    peso = db.Column(db.Float)
    populated = db.Column(db.BOOLEAN, default=False, nullable=False)
    # quotes = db.relationship("Quote", backref="quotes", lazy=True)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, name, symbol, peso):
        self.name = name
        self.symbol = symbol
        self.peso = peso

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Empresa %r>" % self.name
