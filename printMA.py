__author__ = 'Karsten'

import dataStorage
import analysis
import time

print('105 Minuten | 50 Minuten | Differenz')
while True:
    ma_big = dataStorage.get_ma(105)
    ma_small = dataStorage.get_ma(50)
    print(str(ma_big) + ' | ' + str(ma_small) + ' | ' + str(analysis.getDifference(ma_big, ma_small)))
    time.sleep(60)
