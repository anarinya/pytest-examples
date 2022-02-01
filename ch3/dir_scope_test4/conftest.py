# pytest --setup-show test_count.py
# pytest --func-db --setup-show test-count.py
import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
import cards


# when using the --func-db flag, create a new db for each function
def pytest_addoption(parser):
    parser.addoption(
        "--func-db",
        action="store_true",
        default=False,
        help="create a new database for each test"
    )


# if using the --func-db flag create per-function databases, otherwise per-session
def db_scope(fixture_name, config):
    if config.getoption("--func-db", None):
        return "function"
    return "session"


@pytest.fixture(scope=db_scope)
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


@pytest.fixture(scope="session")
def some_cards():
    """List of different Card objects"""
    return [
        cards.Card("write book", "brian", "done"),
        cards.Card("edit book", "katie", "done"),
        cards.Card("write 2nd edition", "brian", "todo"),
        cards.Card("edit 2nd edition", "katie", "todo")
    ]


@pytest.fixture(scope="function")
def non_empty_db(cards_db, some_cards):
    """CardsDB object that's been populated with 'some_cards'"""
    for card in some_cards:
        cards_db.add_card(card)
    return cards_db
