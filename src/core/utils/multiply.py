from decimal import Decimal
from typing import List

from src.core.money.money import get_money
from src.ecbahia.models.route.model import MyBet


def multiply_list(my_odds: List[MyBet]) -> Decimal:
    all_ods = [bet.odd for bet in my_odds]

    multi_odds = Decimal("1.00")

    for odd in all_ods:
        multi_odds *= odd
    else:
        multi_odds = get_money(money=multi_odds)

    return multi_odds
