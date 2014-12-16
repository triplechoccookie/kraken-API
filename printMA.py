__author__ = 'Karsten'

import dataStorage
import time

print('60 Minuten | 10 Minuten')
while True:
    print(str(dataStorage.get_MA(61)) + ' | ' +  str(dataStorage.get_MA(30)))
    time.sleep(60)