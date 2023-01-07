from decimal import Decimal


class InvestChecker:
    @classmethod
    def money_smaller(cls, money: Decimal, cash: Decimal = Decimal("0.00")) -> bool:
        return money < cash

    @classmethod
    def money_greater(cls, money: Decimal, cash: Decimal = Decimal("0.00")) -> bool:
        return money > cash

    @classmethod
    def money_equals(cls, money: Decimal, cash: Decimal = Decimal("0.00")) -> bool:
        return money == cash

    @classmethod
    def time_smaller(cls, time: int, temp: int = 0) -> bool:
        return time < temp

    @classmethod
    def time_greater(cls, time: int, temp: int = 0) -> bool:
        return time > temp

    @classmethod
    def time_equals(cls, time: int, temp: int = 0) -> bool:
        return time == temp

    @classmethod
    def is_string(cls, word: str) -> bool:
        return isinstance(word, str)

    @classmethod
    def is_str_greater(cls, word: str, length: int = 0) -> bool:
        return len(word) > length
