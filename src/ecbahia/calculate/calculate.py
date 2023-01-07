from src.ecbahia.calc_bet.calc_bet import (
    profit, amount, multi_bet, profits
)

from src.ecbahia.models.route.model import Winner as WinRequest
from src.ecbahia.models.data.model import Winner as WinResponse
from src.ecbahia.models.route.model import WinnerMulti
from src.ecbahia.routes.endpoints import Endpoints

e = Endpoints()


class Calculate:
    @classmethod
    def post_earning(cls, winner: WinRequest) -> WinResponse:
        win_response = profit(my_bet=winner)

        return win_response

    @classmethod
    def post_amounts(cls, winner: WinRequest) -> WinResponse:
        win_response = amount(my_bet=winner)

        return win_response

    @classmethod
    def post_multi_earnings(cls, winners: WinnerMulti) -> WinResponse:
        win_response = multi_bet(my_bets=winners)

        return win_response

    @classmethod
    def post_earnings(cls, winner: WinRequest) -> WinResponse:
        win_response = profits(my_bet=winner)

        return win_response
