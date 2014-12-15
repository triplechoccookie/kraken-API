__author__ = 'Karsten'

import krakenAPI
import time

print('starting')


print('Serverzeit ist ' + time.strftime('%a, %d %b %Y %H:%M:%S +0000', krakenAPI.get_server_time()))

print(krakenAPI.get_assets())

lasttimestamp = '0'
while True:
    data = krakenAPI.get_ohcl_data('XLTCZEUR', '1', lasttimestamp)
    for item in data:
        print(item)
    lasttimestamp = data[-1]['timestamp']
    time.sleep(10)


print('closing')