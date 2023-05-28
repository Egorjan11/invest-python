import asyncio
import os

from tinkoff.invest import AsyncClient

token = os.environ["t.PXRpihIQNpKpAsjfJcqOLx-aNz4bC-zHUNP1tmkqAtj3qLZghqrEAGdgPbcH8qt_H2MIQoSSZ0olxJLrhzJg0w"]


async def main():
    async with AsyncClient(token) as client:
        statuses = await client.market_data.get_trading_statuses(
            instrument_ids=["BBG004730N88"]
        )
        print(statuses)


if __name__ == "__main__":
    asyncio.run(main())
