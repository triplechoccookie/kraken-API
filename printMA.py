__author__ = 'Karsten'

import dataStorage
import time

print('60 Minuten | 10 Minuten')
while True:
    print(str(dataStorage.get_MA(60)) + ' | ' +  str(dataStorage.get_MA(10)))
    time.sleep(60)