import os

from tinkoff.invest.sandbox.client import SandboxClient

TOKEN = os.environ["t.PXRpihIQNpKpAsjfJcqOLx-aNz4bC-zHUNP1tmkqAtj3qLZghqrEAGdgPbcH8qt_H2MIQoSSZ0olxJLrhzJg0w"]


def main():
    with SandboxClient(TOKEN) as client:
        print(client.users.get_info())


if __name__ == "__main__":
    main()
