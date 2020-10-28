from datetime import timedelta
from time import strftime

from pytz import timezone

from app import db


class Quote(db.Model):
    __tablename__ = "quotes"

    id = db.Column(db.Integer, primary_key=True)
    price_opened = db.Column(db.Float)
    price_closed = db.Column(db.Float)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    db.UniqueConstraint(
        "quotes.date", "quotes.company_id", name="quote_date_company_constraint"
    )
    # --------------------------------------------------------------------------------------------------#

    def __init__(
        self, date, company_id, price_opened=None, price_closed=None, price=None
    ):
        self.date = date
        self.price_opened = price_opened
        self.price_closed = price_closed
        self.price = price
        self.company_id = company_id

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Cotacao %r>" % self.id

    def dict(self):
        dictret = dict(self.__dict__)
        dictret.pop("_sa_instance_state", None)

        dictret["date"] = int((self.date - timedelta(hours=3)).strftime("%s") + "000")
        return dictret
