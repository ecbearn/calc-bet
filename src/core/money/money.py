from decimal import Decimal


def get_money(money: Decimal = Decimal("0.00")) -> Decimal:
    money = str(money)

    if "." in money:
        dot_decs = money[money.find("."):]
        money = money[: money.find(".")]

        dot_decs = dot_decs[: 3] if len(dot_decs) > 3 else dot_decs
        dot_decs = dot_decs if len(dot_decs) == 3 else f"{dot_decs}0"

        money = f"{money}{dot_decs}"

    else:
        money = f"{money}.00"

    new_money = Decimal(money)

    return new_money
