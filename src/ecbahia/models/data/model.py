from decimal import Decimal

from pydantic.dataclasses import dataclass


@dataclass
class MyBet:
    capital: Decimal
    profit: Decimal
    amount: Decimal
    fee: Decimal
