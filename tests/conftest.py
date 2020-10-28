import pytest
from app import app as _app, db as _db, User
from scripts.recreate_database import recreate_database


@pytest.fixture
def app():
    return _app


@pytest.fixture
def db(app):
    with app.app_context():
        _db.drop_all()
        _db.create_all()
        recreate_database(_db)
        yield _db
        _db.drop_all()
        _db.session.commit()
