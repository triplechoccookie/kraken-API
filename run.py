__author__ = 'Karsten'

import krakenAPI
import dataStorage
import time

def run():

    print('starting')


    print('Serverzeit ist ' + time.strftime('%a, %d %b %Y %H:%M:%S +0000', krakenAPI.get_server_time()))

    lasttimestamp = dataStorage.get_last_data_timestamp()

    print('Letzter Zeitstempel: ' + str(lasttimestamp))

    data = krakenAPI.get_ohcl_data(interval='1', since=str(lasttimestamp))

    for item in data:
        dataStorage.store_new_data(int(item['timestamp']), float(item['high']), float(item['low']), float(item['open']),
                                   float(item['close']), float(item['volume']), float(item['count']))

    newtimestamp = dataStorage.get_last_data_timestamp()

    print('Neuester Zeitstempel: ' + str(newtimestamp))

    print('closing')