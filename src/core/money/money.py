from decimal import Decimal


def get_money(money: Decimal = Decimal("0.00")) -> Decimal:
    money = str(money)

    money = money[: money.find(".") + 3]

    new_money = Decimal(money)

    return new_money
