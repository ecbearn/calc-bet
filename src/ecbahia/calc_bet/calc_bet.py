from src.core.money.money import get_money

from src.core.utils.multiply import multiply_list

from src.ecbahia.models.data.model import MyBet as BetResponse
from src.ecbahia.models.route.model import MyBet as BetRequest
from src.ecbahia.models.route.model import MyBetMulti


def profit(my_bet: BetRequest) -> BetResponse:
    my_profit = my_bet.money * my_bet.odd
    my_profit = get_money(my_profit)

    my_amount = my_bet.money + my_profit
    my_amount = get_money(my_amount)

    bet_response = BetResponse(
        capital=my_bet.money,
        profit=my_profit,
        odd=my_bet.odd
    )

    bet_response.descript = my_bet.descript
    bet_response.time = my_bet.time
    bet_response.is_multi = my_bet.is_multi
    bet_response.amount = my_amount

    return bet_response


def amount(my_bet: BetRequest) -> BetResponse:
    my_profit: BetResponse = BetResponse(
        capital="0",
        profit="0",
        odd="0"
    )

    for time in range(my_bet.time):
        my_profit = profit(my_bet=my_bet)

        my_bet.money = my_profit.amount

    return my_profit


def multi_bet(my_bets: MyBetMulti) -> BetResponse:
    multi_ods = multiply_list(my_odds=my_bets.my_bets)

    total_profit = multi_ods * my_bets.money
    total_profit = get_money(total_profit)

    total_amount = my_bets.money + total_profit
    total_amount = get_money(total_amount)

    bet_response = BetResponse(
        capital=my_bets.money,
        profit=total_profit,
        odd=multi_ods
    )

    bet_response.is_multi = True
    bet_response.descript = "This is a Multiply Bet!"
    bet_response.amount = total_amount

    return bet_response


def profits(my_bet: BetRequest) -> BetResponse:
    my_amount = get_money()
    my_profit = get_money()

    total_profit = get_money()

    total_amount = my_bet.money
    total_amount = get_money(money=total_amount)

    for time in range(my_bet.time):
        my_amount = my_bet.money * my_bet.odd
        my_amount = get_money(money=my_amount)

        my_profit = my_amount - my_bet.money
        my_profit = get_money(money=my_profit)

        total_profit += my_profit
        total_profit = get_money(total_profit)

        total_amount += my_profit
        total_amount = get_money(total_amount)

    bet_response: BetResponse = BetResponse(
        capital=my_bet.money,
        profit=total_profit,
        odd=my_bet.odd
    )

    bet_response.amount = total_amount
    bet_response.is_multi = my_bet.is_multi
    bet_response.descript = "Income fixed Money!"

    return bet_response
