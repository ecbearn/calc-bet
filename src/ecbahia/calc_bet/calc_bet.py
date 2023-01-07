from src.core.money.money import get_money

from src.core.utils.multiply import multiply_list

from src.ecbahia.models.data.model import MyBet as BetResponse
from src.ecbahia.models.route.model import MyBet as BetRequest
from src.ecbahia.models.route.model import MyBetMulti


def profit(my_bet: BetRequest) -> BetResponse:
    my_profit = my_bet.money * my_bet.fee

    my_profit = get_money(money=my_profit)

    bet_response = BetResponse()

    bet_response.profit = my_profit
    bet_response.fee = my_bet.fee
    bet_response.capital = my_bet.money
    bet_response.descript = my_bet.descript
    bet_response.time = my_bet.time
    bet_response.is_multi = my_bet.is_multi

    return bet_response


def amount(my_bet: BetRequest) -> BetResponse:
    my_profit = profit(my_bet=my_bet)

    my_amount = my_profit.profit + my_bet.money

    my_amount = get_money(money=my_amount)

    my_profit.amount = my_amount

    return my_profit


def multi_bet(my_bets: MyBetMulti) -> BetResponse:
    multi_ods = multiply_list(my_odds=my_bets.my_bets)

    bet_response = BetResponse()
    bet_response.is_multi = True
    bet_response.descript = "This is a Multiply Bet!"
    bet_response.fee = multi_ods
    bet_response.capital = my_bets.money

    total_amount = bet_response.fee * bet_response.capital
    total_amount = get_money(total_amount)

    total_profit = total_amount - bet_response.capital
    total_profit = get_money(total_profit)

    bet_response.amount = total_amount
    bet_response.profit = total_profit

    return bet_response
