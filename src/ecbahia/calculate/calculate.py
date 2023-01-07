from src.ecbahia.calc_bet.calc_bet import (
    profit, amount, multi_bet, profits
)

from src.ecbahia.models.route.model import MyBet as BetRequest
from src.ecbahia.models.data.model import MyBet as BetResponse
from src.ecbahia.models.route.model import MyBetMulti


class Calculate:
    @classmethod
    def post_profit(cls, my_bet: BetRequest) -> BetResponse:
        bet_response = profit(my_bet=my_bet)

        return bet_response

    @classmethod
    def post_amount(cls, my_bet: BetRequest) -> BetResponse:
        bet_response = amount(my_bet=my_bet)

        return bet_response

    @classmethod
    def post_multi_bet(cls, my_bets: MyBetMulti) -> BetResponse:
        bet_response = multi_bet(my_bets=my_bets)

        return bet_response

    @classmethod
    def post_profits(cls, my_bet: BetRequest) -> BetResponse:
        bet_response = profits(my_bet=my_bet)

        return bet_response
