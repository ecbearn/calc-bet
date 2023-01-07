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

from src.ecbahia.calculate.calculate import Calculate as Earn


APP_JSON = "application/json"

calc_bet_api = APIRouter()
link = Endpoints()


@calc_bet_api.post(path=link.post_earning, response_model=BetResponse)
def post_earning(my_bet: BetRequest) -> HTMLResponse:
    try:
        Checker.checker(my_bet=my_bet)
    except ValueError as ve:
        raise_http_exception(message=ve.args[0])

    earn_response = Earn.post_profit(my_bet=my_bet)

    response = get_html_response(
        status_code=201,
        content=earn_response.to_dict()
    )

    return response


@calc_bet_api.post(path=link.post_amounts, response_model=BetResponse)
def post_amounts(my_bet: BetRequest) -> HTMLResponse:
    try:
        Checker.checker(my_bet=my_bet, is_multi=True)
    except ValueError as ve:
        raise_http_exception(message=ve.args[0])

    earn_response = Earn.post_amount(my_bet=my_bet)

    response = get_html_response(
        status_code=201,
        content=earn_response.to_dict()
    )

    return response


@calc_bet_api.post(path=link.post_multi_earnings, response_model=BetResponse)
def post_multi_earnings(my_bets: MyBetMulti) -> HTMLResponse:
    try:
        Checker.checker_bet_multi(my_bets=my_bets)
    except ValueError as ve:
        raise_http_exception(message=ve.args[0])

    earn_response = Earn.post_multi_bet(my_bets=my_bets)

    response = get_html_response(
        status_code=201,
        content=earn_response.to_dict()
    )

    return response


@calc_bet_api.post(path=link.post_earnings, response_model=BetResponse)
def post_earnings(my_bet: BetRequest) -> HTMLResponse:
    try:
        Checker.checker(my_bet=my_bet, is_multi=True)
    except ValueError as ve:
        raise_http_exception(message=ve.args[0])

    earn_response = Earn.post_profits(my_bet=my_bet)

    response = get_html_response(
        status_code=201,
        content=earn_response.to_dict()
    )

    return response
