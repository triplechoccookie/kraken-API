__author__ = 'Karsten'

import restHelper
import time


def get_server_time():
    data = restHelper.get_data_from_url('https://api.kraken.com/0/public/Time')
    if data['error'] is []:
        data = time.gmtime(data['result']['unixtime'])
    else:
        data = 0

    return data


def get_assets():
    data = restHelper.get_data_from_url('https://api.kraken.com/0/public/Assets')
    if data['error'] is []:
        data = data['result']
    else:
        data = 0

    return data


def get_ticker(pair='XBTEUR'):
    data = restHelper.get_data_from_url('https://api.kraken.com/0/public/Ticker', {'pair': pair})
    if data['error'] is []:
        data = data['result']
    else:
        data = 0

    return data

def get_ohcl_data(pair='XBTEUR', interval='15', since='0'):
    data = restHelper.get_data_from_url('https://api.kraken.com/0/public/OHLC', {'pair': pair, 'interval': interval,
                                                                                 'since': since})
    if data['error'] is []:
        data = data['result'][pair]
        retval = []
        for item in data:
            retval.append(
                {'timestamp': item[0], 'open': item[1], 'high': item[2], 'low': item[3], 'close': item[4],
                 'volumewap': item[5], 'volume': item[6], 'count': item[7]})
    else:
        retval = 0

    return retval


def get_supported_assets():
    assets = ('XBTEUR', 'XBTLTC')
    return assets