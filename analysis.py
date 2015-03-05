__author__ = 'u2441792'


import dataStorage


sell = 'sell'
noOperation = 'nop'
buy = 'buy'



def simulate_trade_on_ma_crossover_with_fees(big_ma, small_ma, fee=0, money=100):
    bigMAs = dataStorage.get_ma_step_by_step(big_ma, 0, 0)
    smallMAs = dataStorage.get_ma_step_by_step(small_ma, 0, 0)
    prices = dataStorage.get_price_history(0, 0)
    bank = money
    coin = 0.0
    trades = 0

    oldadvice = noOperation

    for i in range(len(bigMAs)):
        diff = getDifference(bigMAs[i], smallMAs[i])
        advice = get_trade_advice_on_difference_with_deadzone(diff, 0.01)

        if advice == oldadvice:
            oldadvice = advice
        elif advice == buy:
            if prices[i] > 0:
                coin += (bank / prices[i]) * (1 - fee)
                bank = 0
                trades += 1
        elif advice == sell:
            if prices[i] > 0:
                bank += (coin * prices[i]) * (1 - fee)
                coin = 0
                trades += 1

    # sell everything at end of simulation
    if coin > 0:
        bank += (coin * prices[-1]) * (1 - fee)
        coin = 0
        trades += 1

    return {'money': bank, 'coins': coin}


def get_trade_advice_on_difference_with_deadzone(diff, deadzone=0):
    if diff > (0 + deadzone):
        return buy
    elif diff < (0 - deadzone):
        return sell
    else:
        return noOperation


def getDifference(first, second):
    return first - second
