__author__ = 'Karsten'

import urllib.request
import json


def get_data_from_URL(url, inputdata={}):
    params = urllib.parse.urlencode(inputdata)
    params = params.encode('utf-8')

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    f = opener.open(url, params)
    datastring = f.read().decode('utf-8')
    output = parse_json(datastring)
    return output


def parse_json(datastring):
    data = json.loads(datastring)
    return data