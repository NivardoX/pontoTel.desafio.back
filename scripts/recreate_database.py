from sqlalchemy import text

from config import ROOT_DIR


def recreate_database(db):
    session = db.session()
    # Open the .sql file
    sql_file = open(ROOT_DIR + "/dml.sql", "r")
    escaped_sql = text(sql_file.read())
    session.execute(escaped_sql)
    session.commit()
    session.close()
