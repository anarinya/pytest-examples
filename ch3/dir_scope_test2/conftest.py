import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
import cards


@pytest.fixture(scope="session")
def db():
    """CardsDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db_ = cards.CardsDB(db_path)
        yield db_
        db_.close()


@pytest.fixture(scope="function")
def cards_db(db):
    """Empty the CardsDB object after each function"""
    db.delete_all()
    return db
