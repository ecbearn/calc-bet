import json
from json import dumps

from typing import Optional

from decimal import Decimal

from pydantic.dataclasses import dataclass


@dataclass
class MyBet:
    capital: Decimal
    profit: Decimal
    odd: Decimal
    amount: Optional[Decimal] = None
    time: Optional[int] = None
    descript: Optional[str] = None
    is_multi: Optional[bool] = False

    def as_json(self) -> json:
        bet = {
            key: value if not isinstance(value, Decimal) else str(value)
            for key, value in self.__dict__.items()
            if key[0] != "_"
        }

        return dumps(bet, indent=4)
