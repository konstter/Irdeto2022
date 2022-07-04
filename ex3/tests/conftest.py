import pytest
from ex3.ex3_domain import Card


@pytest.fixture(scope="module")
def create_card1():
    card1 = Card()
    return card1


@pytest.fixture(scope="module")
def create_card2():
    card2 = Card()
    return card2
