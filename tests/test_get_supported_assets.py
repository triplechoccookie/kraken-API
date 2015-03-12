__author__ = 'Karsten'

import krakenAPI


data = krakenAPI.get_supported_assets()
print(data)