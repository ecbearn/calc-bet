from src.ecbahia.earner.earner import (
    invest, amounts, multi_earning, invests
)

from src.ecbahia.models.route.model import Winner as WinRequest
from src.ecbahia.models.data.model import Winner as WinResponse
from src.ecbahia.models.route.model import WinnerMulti
from src.ecbahia.routes.endpoints import Endpoints

e = Endpoints()


class Calculate:
    @classmethod
    def post_earning(cls, winner: WinRequest) -> WinResponse:
        win_response = invest(winner=winner)

        return win_response

    @classmethod
    def post_amounts(cls, winner: WinRequest) -> WinResponse:
        win_response = amounts(winner=winner)

        return win_response

    @classmethod
    def post_multi_earnings(cls, winners: WinnerMulti) -> WinResponse:
        win_response = multi_earning(winners=winners)

        return win_response

    @classmethod
    def post_earnings(cls, winner: WinRequest) -> WinResponse:
        win_response = invests(winner=winner)

        return win_response
