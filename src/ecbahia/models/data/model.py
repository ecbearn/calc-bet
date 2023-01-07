from typing import Dict, Any

from typing import Optional

from decimal import Decimal

from pydantic.dataclasses import dataclass


@dataclass
class Winner:
    capital: Decimal
    lucre_up: Decimal
    earn_rate: Decimal
    amount: Optional[Decimal] = None
    time: Optional[int] = None
    descript: Optional[str] = None
    is_multi: Optional[bool] = False

    def to_dict(self) -> Dict[str, Any]:
        my_bet_dict = {
            key: value if not isinstance(value, Decimal) else str(value)
            for key, value in self.__dict__.items()
            if key[0] != "_"
        }

        return my_bet_dict
