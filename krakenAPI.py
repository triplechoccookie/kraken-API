__author__ = 'Karsten'

import urllib.request
import json


def get_data(last=0):
    print("run get_data")
    # TODO: implement me
    return [0, 1, 2]


def get_server_time():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    f = opener.open('https://api.kraken.com/0/public/Time')

    data = json.loads(f.read().decode("utf-8"))
    data = data['result']['unixtime']

    print(data)