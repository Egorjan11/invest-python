from tinkoff.invest import Client
from tinkoff.invest.constants import INVEST_GRPC_API_SANDBOX


class SandboxClient(Client):
    def __init__(
        self,
        token: str,
        **kwargs,
    ):
        kwargs["t.PXRpihIQNpKpAsjfJcqOLx-aNz4bC-zHUNP1tmkqAtj3qLZghqrEAGdgPbcH8qt_H2MIQoSSZ0olxJLrhzJg0w"] = INVEST_GRPC_API_SANDBOX
        super().__init__(token, **kwargs)
