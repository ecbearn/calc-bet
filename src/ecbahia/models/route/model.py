from decimal import Decimal

from typing import Optional

from pydantic import BaseModel


class MyBet(BaseModel):
    money: Decimal
    fee: Optional[Decimal] = Decimal("0.20")
