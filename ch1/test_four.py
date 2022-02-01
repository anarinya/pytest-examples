import pytest


@pytest.mark.xfail()
def test_should_fail():
    assert 3 > 5
