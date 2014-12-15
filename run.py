__author__ = 'Karsten'

import krakenAPI
import time

print('starting')


print('Serverzeit ist ' + time.strftime('%a, %d %b %Y %H:%M:%S +0000', krakenAPI.get_server_time()))

print(krakenAPI.get_assets())

print(krakenAPI.get_ticker('XXBTZEUR'))


print('closing')