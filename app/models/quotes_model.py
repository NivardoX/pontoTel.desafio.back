from app import db


class Quote(db.Model):
    __tablename__ = "quotes"

    id = db.Column(db.Integer, primary_key=True)
    price_opened = db.Column(db.Float)
    price_closed = db.Column(db.Float)
    price = db.Column(db.Float)
    type = db.Column(db.String(50),nullable=False)
    date = db.Column(db.DateTime,nullable=False,unique=True)
    company_id = db.column(db.Integer,db.ForeignKey('companies.id'),unique=True)
    # company = db.relationship('Company', backref="companies_id", lazy=True)




    # --------------------------------------------------------------------------------------------------#

    def __init__(self,date,type,company_id,price_opened=None, price_closed=None, price=None):
        self.date = date
        self.type = type
        self.price_opened = price_opened
        self.price_closed = price_closed
        self.price = price
        self.company_id = company_id



    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Cotacao %r>" % self.id
