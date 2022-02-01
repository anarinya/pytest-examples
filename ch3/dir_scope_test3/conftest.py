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
