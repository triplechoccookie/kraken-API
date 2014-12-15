__author__ = 'Karsten'

import krakenAPI
import time

print('starting')


print('Serverzeit ist ' + time.strftime('%a, %d %b %Y %H:%M:%S +0000', krakenAPI.get_server_time()))

print(krakenAPI.get_assets())

lasttimestampXBT = '0'
lasttimestampLTC = '0'
while True:
    data = krakenAPI.get_ohcl_data('XLTCZEUR', '1', lasttimestampLTC)
    if lasttimestampLTC != data[-1]['timestamp']:
        lasttimestampLTC = data[-1]['timestamp']
        print('EUR/LTC')
        for item in data:
            print(item)

    data = krakenAPI.get_ohcl_data('XXBTZEUR', '1', lasttimestampXBT)
    if lasttimestampXBT != data[-1]['timestamp']:
        lasttimestampXBT = data[-1]['timestamp']
        print('EUR/XBT')
        for item in data:
            print(item)

    time.sleep(5)


print('closing')