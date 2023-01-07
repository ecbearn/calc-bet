from decimal import Decimal

from src.ecbahia.models.route.model import Winner, WinnerMulti

from src.core.checkers.checker import InvestChecker as WinChecker


class WinnerValidator:
    @classmethod
    def checker(cls, winner: Winner, is_multi: bool = False) -> None:
        if winner.descript is not None:
            if not WinChecker.is_string(word=winner.descript):
                raise ValueError("error: descript must be an string.")

            elif not WinChecker.is_str_greater(word=winner.descript):
                raise ValueError("error: descript must be greater than 0.")

        elif is_multi:
            if not winner.is_multi:
                raise ValueError("error: is_multi parameter must be true.")

            elif not WinChecker.time_greater(time=winner.time, temp=1):
                raise ValueError("error: time parameter must be greater than 1 for is_multi true.")

        elif WinChecker.time_equals(time=winner.time):
            raise ValueError("error: time must be greater than 0.")

        elif not WinChecker.money_greater(money=winner.money):
            raise ValueError("error: money must be greater than 0.")
        elif not WinChecker.money_greater(money=winner.earn_rate):
            raise ValueError("error: fee must be greater than 0.")

    @classmethod
    def checker_multi_earn(cls, winners: WinnerMulti) -> None:
        if WinChecker.money_smaller(money=winners.money, cash=winners.min_money):
            raise ValueError("error: your investment doesn't match the minimal value.")

        elif len(winners.my_earnings) == 0:
            raise ValueError("error: you don't have any odd to calculate.")

        checker = map(lambda e: e.earn_rate < Decimal("0.01") or not e.is_multi, winners.my_earnings)

        if next(checker):
            raise ValueError(f"error: it was found a invalid earn rate.")
