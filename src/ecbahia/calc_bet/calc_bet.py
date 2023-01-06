from decimal import Decimal

from src.core.money import get_money


def profit(money: Decimal, fee: Decimal) -> Decimal:
    my_profit = money * fee

    my_profit = get_money(money=my_profit)

    return my_profit


def amount(money: Decimal, fee: Decimal) -> Decimal:
    my_amount = profit(money=money, fee=fee) * money

    my_amount = get_money(money=my_amount)

    return my_amount
