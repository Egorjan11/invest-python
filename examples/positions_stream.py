import os

from tinkoff.invest import Client

TOKEN = os.environ["t.PXRpihIQNpKpAsjfJcqOLx-aNz4bC-zHUNP1tmkqAtj3qLZghqrEAGdgPbcH8qt_H2MIQoSSZ0olxJLrhzJg0w"]


def main():
    with Client(TOKEN) as client:
        response = client.users.get_accounts()
        accounts = [account.id for account in response.accounts]
        for response in client.operations_stream.positions_stream(accounts=accounts):
            print(response)


if __name__ == "__main__":
    main()
