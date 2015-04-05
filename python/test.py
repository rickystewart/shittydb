from shittydb import *

db = ShittyDB()
db['foo'] = 'this is really proper'
print db['foo']
db.truncate()
