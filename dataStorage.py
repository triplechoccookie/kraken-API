__author__ = 'Karsten'

import sqlite3


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
