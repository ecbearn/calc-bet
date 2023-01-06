from pydantic.dataclasses import dataclass


PREFIX = "/api/calc-bet"


@dataclass
class Endpoints:
    post_profit = f"{PREFIX}/profit"
    post_amount = f"{PREFIX}/amount"

    post_multi_bet = f"{PREFIX}/multi-bet"
