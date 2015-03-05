__author__ = 'Karsten'

import sqlite3
import math

# constants
DATABASE = 'database.db'
DEFAULT_ASSET_PAIR = 'XBTEUR'


def create_table(asset_pair=DEFAULT_ASSET_PAIR):

    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()
    c.execute('''CREATE TABLE ''' + asset_pair + ''' (timestamp INTEGER PRIMARY KEY, high REAL, low REAL, open REAL,
              close REAL, volume REAL, count REAL)''')
    c.execute('REPLACE INTO ' + asset_pair + ' VALUES (0,0,0,0,0,0,0)')
    connection.commit()
    connection.close()


def get_last_data_timestamp(asset_pair=DEFAULT_ASSET_PAIR):
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()
    c.execute('SELECT MAX(timestamp) FROM' + asset_pair)
    data = c.fetchall()
    connection.close()

    if data[0][0] is not None:
        return data[0][0]
    else:
        return 0


def store_new_data(timestamp, high, low, opening, close, volume, count, asset_pair=DEFAULT_ASSET_PAIR):
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()
    data = (timestamp, high, low, opening, close, volume, count)
    c.execute('REPLACE INTO ' + asset_pair + ' VALUES (?,?,?,?,?,?,?)', data)
    connection.commit()
    connection.close()


def get_ma(length, asset_pair=DEFAULT_ASSET_PAIR):
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()

    data = (length, )
    c.execute('SELECT close FROM ' + asset_pair + ' ORDER BY timestamp DESC LIMIT ?', data)
    retdata = c.fetchall()

    ma = 0.0
    for item in retdata:
        ma += float(item[0])
    ma = ma / length

    return ma


def get_ma_step_by_step(length, starting_timestamp, stopping_timestamp, asset_pair=DEFAULT_ASSET_PAIR):
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()

    c.execute('SELECT close FROM ' + asset_pair + ' ORDER BY timestamp DESC')
    retdata = c.fetchall()

    malist = []
    prices = []
    for i in range(len(retdata)):
        tmp = retdata[i:(i+length)]
        for item in tmp:
            prices.append(item[0])
        malist.append(average(prices))

    return malist


def get_price_history(starting_timstamp, stopping_timestamp, asset_pair=DEFAULT_ASSET_PAIR):
    connection = sqlite3.connect(DATABASE)
    c = connection.cursor()

    c.execute('SELECT close FROM ' + asset_pair + ' ORDER BY timestamp DESC')

    retdata = []
    for item in c.fetchall():
        retdata.append(item[0])

    return retdata


def average(values):
    return math.fsum(values) / len(values)
