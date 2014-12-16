__author__ = 'Karsten'

import sqlite3


def init_storage():
    connection = sqlite3.connect('database.db')
    c = connection.cursor()
    c.execute('''CREATE TABLE ohcl_1m (timestamp INTEGER PRIMARY KEY, high INTEGER, low INTEGER, open INTEGER,
              close INTEGER, volume INTEGER, count INTEGER)''')
    connection.commit()

    connection.close()


def get_last_data_timestamp():
    connection = sqlite3.connect('database.db')
    c = connection.cursor()
    c.execute('SELECT MAX(timestamp) FROM ohcl_1m')
    data = c.fetchall()
    connection.close()

    return data[0][0]


def store_new_data(timestamp, high, low, open, close, volume, count):
    connection = sqlite3.connect('database.db')
    c = connection.cursor()

    data = (timestamp, high, low, open, close, volume, count)

    c.execute('REPLACE INTO ohcl_1m VALUES (?,?,?,?,?,?,?)', data)

    connection.commit()

    connection.close()
