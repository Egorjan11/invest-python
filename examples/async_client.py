import asyncio
import os

from tinkoff.invest import AsyncClient

TOKEN = os.environ["t.PXRpihIQNpKpAsjfJcqOLx-aNz4bC-zHUNP1tmkqAtj3qLZghqrEAGdgPbcH8qt_H2MIQoSSZ0olxJLrhzJg0w"]


async def main():
    async with AsyncClient(TOKEN) as client:
        print(await client.users.get_accounts())


if __name__ == "__main__":
    asyncio.run(main())
