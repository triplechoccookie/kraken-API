__author__ = 'Karsten'

import fetchKrakenData
import time

while True:
    fetchKrakenData.run()
    time.sleep(30)