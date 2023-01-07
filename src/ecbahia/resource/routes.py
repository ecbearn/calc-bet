from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from src.core.utils.response import (
    get_html_response,
    raise_http_exception
)

from src.ecbahia.routes.endpoints import Endpoints

from src.ecbahia.models.route.model import MyBet as BetRequest
from src.ecbahia.models.data.model import MyBet as BetResponse
from src.ecbahia.models.route.model import MyBetMulti

from src.ecbahia.controller.controller import MyBetValidator as Checker

from src.ecbahia.calculate.calculate import Calculate as Profit


APP_JSON = "application/json"

calc_bet_api = APIRouter()
link = Endpoints()


@calc_bet_api.post(path=link.post_profit, response_model=BetResponse)
def post_profit(my_bet: BetRequest) -> HTMLResponse:
    try:
        Checker.checker(my_bet=my_bet)
    except ValueError as ve:
        raise_http_exception(message=ve.args[0])

    bet_response = Profit.post_profit(my_bet=my_bet)

    response = get_html_response(
        status_code=201,
        content=bet_response.to_dict()
    )

    return response


@calc_bet_api.post(path=link.post_amount, response_model=BetResponse)
def post_amount(my_bet: BetRequest) -> HTMLResponse:
    try:
        Checker.checker(my_bet=my_bet)
    except ValueError as ve:
        raise_http_exception(message=ve.args[0])

    bet_response = Profit.post_amount(my_bet=my_bet)

    response = get_html_response(
        status_code=201,
        content=bet_response.to_dict()
    )

    return response


@calc_bet_api.post(path=link.post_multi_bet, response_model=BetResponse)
def post_multi_bet(my_bets: MyBetMulti) -> HTMLResponse:
    try:
        Checker.checker_bet_multi(my_bets=my_bets)
    except ValueError as ve:
        raise_http_exception(message=ve.args[0])

    bet_response = Profit.post_multi_bet(my_bets=my_bets)

    response = get_html_response(
        status_code=201,
        content=bet_response.to_dict()
    )

    return response


@calc_bet_api.post(path=link.post_profits, response_model=BetResponse)
def post_profits(my_bet: BetRequest) -> HTMLResponse:
    try:
        Checker.checker(my_bet=my_bet)
    except ValueError as ve:
        raise_http_exception(message=ve.args[0])

    bet_response = Profit.post_profits(my_bet=my_bet)

    response = get_html_response(
        status_code=201,
        content=bet_response.to_dict()
    )

    return response
