__author__ = 'u2441792'


import dataStorage


sell = 'sell'
noOperation = 'nop'
buy = 'buy'



def simulateTradeOnMaCrossoverWithFees(bigMA, smallMA, fee = 0, money = 100):
    bigMAs = dataStorage.getMaStepByStep(bigMA, 0, 0)
    smallMAs = dataStorage.getMaStepByStep(smallMA, 0, 0)
    prices = dataStorage.getPriceHistory(0, 0)
    bank = money
    coin = 0.0
    trades = 0

    for i in range(len(bigMAs)):
        diff = getDifference(bigMAs[i], smallMAs[i])
        advice = getTradeAdviceOnDifferenceWithDeadZone(diff, 0.01)
        oldadvice = noOperation

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

    #sell everything at end of simulation
    if coin > 0:
        bank += (coin * prices[i]) * (1 - fee)
        coin = 0
        trades += 1

    return {'money': bank, 'coins': coin}


def getTradeAdviceOnDifferenceWithDeadZone(diff, deadzone = 0):
    if(diff > (0 + deadzone)):
        return buy
    elif(diff < (0 - deadzone)):
        return sell
    else:
        return noOperation


def getDifference(first, second):
    return first - second
