__author__ = 'Karsten'

import restHelper
import time


def get_server_time():
    data = restHelper.get_data_from_URL('https://api.kraken.com/0/public/Time')

    unixtime = data['result']['unixtime']

    return time.gmtime(unixtime)


def get_assets():
    data = restHelper.get_data_from_URL('https://api.kraken.com/0/public/Assets')

    return data


def get_ticker(pair='XXBTZEUR'):
    data = restHelper.get_data_from_URL('https://api.kraken.com/0/public/Ticker', {'pair': pair})

    return data

