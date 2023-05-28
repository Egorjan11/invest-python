import os

from tinkoff.invest import Client

TOKEN = os.environ["t.PXRpihIQNpKpAsjfJcqOLx-aNz4bC-zHUNP1tmkqAtj3qLZghqrEAGdgPbcH8qt_H2MIQoSSZ0olxJLrhzJg0w"]


def main():
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts()
        for portfolio in client.operations_stream.portfolio_stream(
            accounts=[acc.id for acc in accounts.accounts]
        ):
            print(portfolio)


if __name__ == "__main__":
    main()
