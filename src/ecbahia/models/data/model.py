from typing import Optional

from decimal import Decimal

from pydantic.dataclasses import dataclass


@dataclass
class MyBet:
    capital: Decimal
    profit: Decimal
    amount: Optional[Decimal] = None
    time: Optional[int] = None
    descript: Optional[int] = None
    fee: Decimal
