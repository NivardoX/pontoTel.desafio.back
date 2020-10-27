import traceback

import matplotlib.pyplot as plt
import pandas as pd

from app import db, Company
from app.components.yahooApi import YahooApi
from app.models.quotes_model import Quote


class TimeSeries:
    def __init__(self, data, symbol):
        self.data = pd.DataFrame(data)
        print(self.data)
        self.symbol = symbol

    def insert(self, start=None):
        session = db.session()
        data_x = []
        data_open_y = []
        data_close_y = []

        for k, v in self.data.get("open", {}).items():
            data_x.append(k[-1])
            data_open_y.append(v)
        for k, v in self.data.get("close", {}).items():
            data_close_y.append(v)
        for (date, opened, closed) in zip(data_x, data_open_y, data_close_y):
            company = (
                session.query(Company).filter(Company.symbol == self.symbol).first()
            )
            if start is not None:
                if start < date:
                    quote = Quote(
                        date,
                        company.id,
                        price_opened=opened,
                        price_closed=closed,
                        price=None,
                    )
                    session.add(quote)

        try:
            session.commit()
        except Exception:
            traceback.print_exc()
        finally:
            session.expunge_all()
            session.close()

    def plot(self):
        data_open_x = []
        data_open_y = []
        data_close_x = []
        data_close_y = []

        for k, v in self.data["open"].items():
            data_open_x.append(k[-1])
            data_open_y.append(v)
        for k, v in self.data["close"].items():
            data_close_x.append(k[-1])
            data_close_y.append(v)

        plt.plot(data_open_x, data_open_y)
        plt.plot(data_close_x, data_close_y)

        plt.show()


if __name__ == "__main__":
    data = YahooApi("^BVSP").ticker.history(period="1mo", interval="1m")
    TimeSeries(data, "^BVSP").insert()
