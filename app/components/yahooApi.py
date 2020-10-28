import json
import traceback

from pandas import DataFrame
from yahooquery import Ticker, search, get_trending

from app.components.exceptions.SymbolNotFoundException import SymbolNotFoundException
from app.components.wrappers.symbol_required import symbol_required
from typing import Optional


class YahooApi:
    def __init__(self, symbol: Optional[str] = None) -> None:

        self.symbol = symbol
        self.ticker = Ticker(self.symbol)
        if symbol:
            try:
                self.check_symbol(symbol)
            except SymbolNotFoundException:
                if not str(symbol).endswith(".SA"):
                    self.symbol = symbol + ".SA"
                    self.ticker = Ticker(self.symbol)
                    self.check_symbol(self.symbol)

                else:
                    raise

    def check_symbol(self, symbol: str) -> None:
        print("CHECANDO {}".format(symbol))
        price = self.ticker.price
        print(price)
        if type(price[symbol]) != dict:
            raise SymbolNotFoundException(price[symbol])

    def extract_prefix(self, symbol: str) -> str:
        if symbol.endswith(".SA"):
            return symbol.split(".")[0]
        else:
            return symbol

    @symbol_required
    def get_price(self) -> float:
        price = self.ticker.price
        if type(price[self.symbol]) != dict:
            raise SymbolNotFoundException(price[self.symbol])
        market_price = price[self.symbol].get("regularMarketPrice", None)
        try:
            float(market_price)
            return market_price
        except:
            traceback.print_exc()
            raise Exception("An error occured when reading the price")

    def get_history(self, period) -> DataFrame:

        return self.ticker.history(period)

    @symbol_required
    def get_details(self) -> dict:
        summary_detail = self.ticker.summary_detail
        if type(summary_detail) != dict:
            raise Exception

        return self.ticker.summary_detail

    @symbol_required
    def historic(self, period, interval) -> DataFrame:
        return self.ticker.history(period=period, interval=interval)


if __name__ == "__main__":
    print(YahooApi("^BVSP").ticker.history("1mo", "5m"))
