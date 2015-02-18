__author__ = 'Karsten'

import analysis


for i in range(1, 100):
    print(i)
    for j in range(1, 100):
        if i > j:
            result = analysis.simulateTradeOnMaCrossoverWithFees(i, j, 0.002, 100)
            if result['money'] >= 100:
                print(str(i) + '/' + str(j) + ': ' + str(result))