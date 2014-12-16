__author__ = 'Karsten'

import sqlite3

connection = sqlite3.connect('database.db')
c = connection.cursor()

def init_storage():
    c.execute('''CREATE TABLE ohcl_1m (timestamp INTEGER PRIMARY KEY, high INTEGER, low INTEGER, open INTEGER,
              close INTEGER, volume INTEGER, count INTEGER)''')
    connection.commit()

def get_last_data_timestamp():
    c.execute('SELECT * FROM ohcl_1m')
    print(c.fetchall())


# def store_new_data():
