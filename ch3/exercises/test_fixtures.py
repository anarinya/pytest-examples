import pytest


@pytest.fixture(name="sandwich_data", scope="module")
def example_data_fixture():
    """Example sandwich data"""
    print('\nsetup sandwich data')
    yield ['cheese', 'bread', 'mustard', 'turkey']
    print('\ndone with sandwich data')


@pytest.fixture(name="people_data")
def people_data_fixture():
    """Example people data"""
    return ['matt', 'leo', 'brittney']


def test_sandwich_data(sandwich_data):
    expected = ['cheese', 'bread', 'mustard', 'turkey']
    assert sandwich_data == expected


def test_sandwich_data_order(sandwich_data):
    assert sandwich_data[0] == 'cheese'


def test_people_data(people_data):
    expected = ['matt', 'leo', 'brittney']
    assert people_data == expected
