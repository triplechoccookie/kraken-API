__author__ = 'Karsten'

import krakenAPI
import dataStorage
import time

lasttimestamp = dataStorage.get_last_data_timestamp()

data = krakenAPI.get_ohcl_data(interval='1', since=str(lasttimestamp-1))

for item in data:
    dataStorage.store_new_data(int(item['timestamp']), float(item['high']), float(item['low']), float(item['open']),
                               float(item['close']), float(item['volume']), float(item['count']))

newtimestamp = dataStorage.get_last_data_timestamp()
