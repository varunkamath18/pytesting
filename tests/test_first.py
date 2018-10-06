import pytest
from resources import first


@pytest.mark.xfail()
def test_fail_helloWorld():
    assert first.helloWorld() == "Hello World"


def test_helloWorld():
    assert first.helloWorld() == "Hello World!"


# Coming soon
@pytest.mark.skip()
def test_goodMorning():
    assert first.goodMorning() == "Good Morning!"
