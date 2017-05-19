from tinydb import TinyDB, where

db = TinyDB('db.json')
db.insert({'saranpong': 'kom'})


text = 'saranpong'
sch = db.search(where(text))

print sch