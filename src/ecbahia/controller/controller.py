from src.ecbahia.models.route.model import MyBet

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
