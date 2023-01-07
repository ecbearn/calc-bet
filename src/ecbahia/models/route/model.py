from decimal import Decimal

from typing import Optional, List

from pydantic import BaseModel


class MyBet(BaseModel):
    money: Decimal = Decimal("0.00")
    descript: Optional[str] = None
    time: Optional[int] = 1
    odd: Optional[Decimal] = Decimal("0.20")
    is_multi: Optional[bool] = False


class MyBetMulti(BaseModel):
    money: Decimal = Decimal("0.00")
    min_money: Decimal = Decimal("0.50")
    my_bets: List[MyBet]
