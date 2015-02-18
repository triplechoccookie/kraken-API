__author__ = 'Karsten'

import sqlite3
import math


def init_storage():
    connection = sqlite3.connect('database.db')
    c = connection.cursor()
    c.execute('''CREATE TABLE ohcl_1m (timestamp INTEGER PRIMARY KEY, high REAL, low REAL, open REAL,
              close REAL, volume REAL, count REAL)''')
    c.execute('REPLACE INTO ohcl_1m VALUES (0,0,0,0,0,0,0)')
    connection.commit()
    connection.close()


def get_last_data_timestamp():
    connection = sqlite3.connect('database.db')
    c = connection.cursor()
    c.execute('SELECT MAX(timestamp) FROM ohcl_1m')
    data = c.fetchall()
    connection.close()

    if data[0][0] != None:
        return data[0][0]
    else:
        return 0


def store_new_data(timestamp, high, low, open, close, volume, count):
    connection = sqlite3.connect('database.db')
    c = connection.cursor()
    data = (timestamp, high, low, open, close, volume, count)
    c.execute('REPLACE INTO ohcl_1m VALUES (?,?,?,?,?,?,?)', data)
    connection.commit()
    connection.close()


def get_MA(length):
    connection = sqlite3.connect('database.db')
    c = connection.cursor()

    data = (length, )
    c.execute('SELECT close FROM ohcl_1m ORDER BY timestamp DESC LIMIT ?', data)
    retdata = c.fetchall()

    ma = 0.0
    for item in retdata:
        ma += float(item[0])
    ma = ma / length

    return ma


def getMaStepByStep(length, startingTimestamp, stoppingTimestamp):
    connection = sqlite3.connect('database.db')
    c = connection.cursor()

    c.execute('SELECT close FROM ohcl_1m ORDER BY timestamp DESC')
    retdata = c.fetchall()

    malist = []
    prices = []
    for i in range(len(retdata)):
        tmp = retdata[i:(i+length)]
        for item in tmp:
            prices.append(item[0])
        malist.append(average(prices))

    return malist

def getPriceHistory(startingTimstamp, stoppingTimestamp):
    connection = sqlite3.connect('database.db')
    c = connection.cursor()

    c.execute('SELECT close FROM ohcl_1m ORDER BY timestamp DESC')

    retdata = []
    for item in c.fetchall():
        retdata.append(item[0])

    return retdata


def average(values):
    return math.fsum(values) / len(values)
