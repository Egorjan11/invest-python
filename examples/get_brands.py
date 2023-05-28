import os

from tinkoff.invest import Client

TOKEN = os.environ["t.PXRpihIQNpKpAsjfJcqOLx-aNz4bC-zHUNP1tmkqAtj3qLZghqrEAGdgPbcH8qt_H2MIQoSSZ0olxJLrhzJg0w"]


def main():
    with Client(TOKEN) as client:
        r = client.instruments.get_brands()
        for brand in r.brands:
            print(brand)


if __name__ == "__main__":
    main()
