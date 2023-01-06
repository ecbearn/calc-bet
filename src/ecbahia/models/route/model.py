from decimal import Decimal

from typing import Optional

from pydantic import BaseModel


class MyBet(BaseModel):
    money: Decimal
    descript: Optional[str] = None
    time: Optional[int] = 1
    fee: Optional[Decimal] = Decimal("0.20")
