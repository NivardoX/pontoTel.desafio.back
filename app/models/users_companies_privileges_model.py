from app import db


class UserCompanyPrivilege(db.Model):
    __tablename__ = "user_company_privileges"

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, user_id, company_id):
        self.user_id = user_id
        self.company_id = company_id

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<UserCompanyPrivilege %r>" % self.id
