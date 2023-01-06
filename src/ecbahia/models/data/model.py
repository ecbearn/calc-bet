from typing import Optional

from decimal import Decimal

from pydantic.dataclasses import dataclass


@dataclass
class MyBet:
    capital: Decimal
    profit: Decimal
    fee: Decimal
    amount: Optional[Decimal] = None
    time: Optional[int] = None
    descript: Optional[int] = None
    is_multi: Optional[bool] = False
