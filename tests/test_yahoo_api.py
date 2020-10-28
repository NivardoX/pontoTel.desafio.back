from app.components.exceptions.SymbolNotDefinedException import (
    SymbolNotDefinedException,
)
from app.components.exceptions.SymbolNotFoundException import SymbolNotFoundException
from app.components.yahooApi import YahooApi
import pytest


def test_get_price():
    price = YahooApi("^BVSP").get_price()
    assert isinstance(price, float)


def test_get_price_symbol_error():
    with pytest.raises(SymbolNotFoundException):
        YahooApi("teste").get_price()


def test_get_price_symbol_error():
    with pytest.raises(SymbolNotDefinedException):
        YahooApi().get_price()


def test_get_details():
    details = YahooApi("^BVSP").get_details()
    print(details)
    assert isinstance(details, dict)
