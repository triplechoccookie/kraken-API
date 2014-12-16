__author__ = 'Karsten'

import dataStorage
import time

print('105 Minuten | 50 Minuten | Differenz')
while True:
    ma_big = dataStorage.get_MA(105)
    ma_small = dataStorage.get_MA(50)
    print(str(ma_big) + ' | ' +  str(ma_small) + ' | ' + str(ma_small - ma_big))
    time.sleep(60)
