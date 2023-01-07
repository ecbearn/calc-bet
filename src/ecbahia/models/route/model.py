from decimal import Decimal

from typing import Optional, List

from pydantic import BaseModel


class Winner(BaseModel):
    money: Decimal = Decimal("0.00")
    descript: Optional[str] = None
    time: Optional[int] = 1
    earn_rate: Optional[Decimal] = Decimal("0.20")
    is_multi: Optional[bool] = False


class WinnerMulti(BaseModel):
    money: Decimal = Decimal("0.00")
    min_money: Decimal = Decimal("0.50")
    my_earnings: List[Winner]
