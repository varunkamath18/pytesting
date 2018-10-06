import pytest  # noqa
from resources import first


def test_helloWorld():
    assert first.helloWorld() == "Hello World"
