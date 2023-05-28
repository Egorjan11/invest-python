import os

from tinkoff.invest import Client

token = os.environ["t.PXRpihIQNpKpAsjfJcqOLx-aNz4bC-zHUNP1tmkqAtj3qLZghqrEAGdgPbcH8qt_H2MIQoSSZ0olxJLrhzJg0w"]


with Client(token) as client:
    statuses = client.market_data.get_trading_statuses(instrument_ids=["BBG004730N88"])
    print(statuses)
