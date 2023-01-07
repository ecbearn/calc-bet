from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from src.core.utils.response import (
    get_html_response,
    raise_http_exception
)

from src.ecbahia.routes.endpoints import Endpoints

from src.ecbahia.models.route.model import Winner as WinRequest
from src.ecbahia.models.data.model import Winner as WinResponse
from src.ecbahia.models.route.model import WinnerMulti

from src.ecbahia.controller.controller import MyBetValidator as Checker

from src.ecbahia.calculate.calculate import Calculate as Earn


calc_bet_api = APIRouter()
link = Endpoints()


@calc_bet_api.post(path=link.post_earning, response_model=WinResponse)
def post_earning(winner: WinRequest) -> HTMLResponse:
    try:
        Checker.checker(my_bet=winner)
    except ValueError as ve:
        raise_http_exception(message=ve.args[0])

    earn_response = Earn.post_earning(winner=winner)

    response = get_html_response(
        status_code=201,
        content=earn_response.to_dict()
    )

    return response


@calc_bet_api.post(path=link.post_amounts, response_model=WinResponse)
def post_amounts(winner: WinRequest) -> HTMLResponse:
    try:
        Checker.checker(my_bet=winner, is_multi=True)
    except ValueError as ve:
        raise_http_exception(message=ve.args[0])

    earn_response = Earn.post_amounts(winner=winner)

    response = get_html_response(
        status_code=201,
        content=earn_response.to_dict()
    )

    return response


@calc_bet_api.post(path=link.post_multi_earnings, response_model=WinResponse)
def post_multi_earnings(winners: WinnerMulti) -> HTMLResponse:
    try:
        Checker.checker_bet_multi(my_bets=winners)
    except ValueError as ve:
        raise_http_exception(message=ve.args[0])

    earn_response = Earn.post_multi_earnings(winners=winners)

    response = get_html_response(
        status_code=201,
        content=earn_response.to_dict()
    )

    return response


@calc_bet_api.post(path=link.post_earnings, response_model=WinResponse)
def post_earnings(winner: WinRequest) -> HTMLResponse:
    try:
        Checker.checker(my_bet=winner, is_multi=True)
    except ValueError as ve:
        raise_http_exception(message=ve.args[0])

    earn_response = Earn.post_earnings(winner=winner)

    response = get_html_response(
        status_code=201,
        content=earn_response.to_dict()
    )

    return response
