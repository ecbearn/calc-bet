from src.core.money.money import get_money

from src.core.utils.multiply import multiply_list

from src.ecbahia.models.data.model import Winner as WinResponse
from src.ecbahia.models.route.model import Winner as WinRequest
from src.ecbahia.models.route.model import WinnerMulti


def invest(winner: WinRequest) -> WinResponse:
    my_earn = winner.money * winner.earn_rate
    my_earn = get_money(my_earn)

    my_amount = winner.money + my_earn
    my_amount = get_money(my_amount)

    win_response = WinResponse(
        capital=winner.money,
        lucre_up=my_earn,
        earn_rate=winner.earn_rate
    )

    win_response.descript = winner.descript
    win_response.time = winner.time
    win_response.is_multi = winner.is_multi
    win_response.amount = my_amount

    return win_response


def amounts(winner: WinRequest) -> WinResponse:
    my_earn: WinResponse = WinResponse(
        capital="0",
        lucre_up="0",
        earn_rate="0"
    )

    for time in range(winner.time):
        my_earn = invest(winner=winner)

        winner.money = my_earn.amount

    return my_earn


def multi_earning(winners: WinnerMulti) -> WinResponse:
    multi_rates = multiply_list(my_odds=winners.my_earnings)

    total_earn = multi_rates * winners.money
    total_earn = get_money(total_earn)

    total_amount = winners.money + total_earn
    total_amount = get_money(total_amount)

    win_response = WinResponse(
        capital=winners.money,
        lucre_up=total_earn,
        earn_rate=multi_rates
    )

    win_response.is_multi = True
    win_response.descript = "This is a Multiply Bet!"
    win_response.amount = total_amount

    return win_response


def invests(winner: WinRequest) -> WinResponse:
    my_amount = get_money()
    my_earn = get_money()

    total_earn = get_money()

    total_amount = winner.money
    total_amount = get_money(money=total_amount)

    for time in range(winner.time):
        my_earn = winner.money * winner.earn_rate
        my_earn = get_money(money=my_earn)

        total_earn += my_earn
        total_earn = get_money(total_earn)

        total_amount += my_earn
        total_amount = get_money(total_amount)

    win_response: WinResponse = WinResponse(
        capital=winner.money,
        lucre_up=total_earn,
        earn_rate=winner.earn_rate
    )

    win_response.amount = total_amount
    win_response.is_multi = winner.is_multi
    win_response.descript = "Income fixed Money!"

    return win_response
