# Created by Admin at 5/8/2022
from collections import ChainMap
default_connection = {'host': 'localhost', 'port': 4567}
connection = {'port': 5678}
conn = ChainMap(connection, default_connection)
conn['host'] = 'packtpub.com'
