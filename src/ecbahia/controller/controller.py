from decimal import Decimal

from src.ecbahia.models.route.model import MyBet, MyBetMulti

from src.core.checkers.checker import MyBetChecker as BetChk


class MyBetValidator:
    @classmethod
    def checker(cls, my_bet: MyBet) -> None:
        if my_bet.descript is not None:
            if not BetChk.is_string(word=my_bet.descript):
                raise ValueError("error: descript must be an string.")

        if not BetChk.is_str_greater(word=my_bet.descript):
            raise ValueError("error: descript must be greater than 0.")

        elif BetChk.time_equals(time=my_bet.time):
            raise ValueError("error: time must be greater than 0.")

        elif not BetChk.money_greater(money=my_bet.money):
            raise ValueError("error: money must be greater than 0.")
        elif not BetChk.money_greater(money=my_bet.fee):
            raise ValueError("error: fee must be greater than 0.")

    @classmethod
    def checker_bet_multi(cls, my_bets: MyBetMulti) -> None:
        if BetChk.money_smaller(money=my_bets.money, cash=my_bets.min_money):
            raise ValueError("error: your bet doesn't match the minimal value.")

        elif len(my_bets.my_bets) == 0:
            raise ValueError("error: you don't have any odd to calculate.")

        checker = map(lambda e: e.fee > Decimal("0.99") and e.is_multi, my_bets.my_bets)
        checker = tuple(c for c in checker)

        if len(checker) < 1:
            raise ValueError("error: it was found a invalid bet odd.")
