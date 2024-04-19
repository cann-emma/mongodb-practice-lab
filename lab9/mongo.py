#!/usr/bin/env python3

from pymongo import MongoClient, errors
import os
from db import *

stats= client.stats
print(stats)

db= client.zgb8ts
coll= db.list_collection_names()
print(coll)

books= db.books
books.insert_many([{"name": "Japanese Tales", "author": ["Multiple", "Royall Tyler"], "genre": "Fairytale and Folklore", "isbn": "56568"}, 
{"name": "Idiot Verse", "author": "Keaton Henson", "genre": "Poetry", "isbn": "98842"},
{"name": "Completing Distinctions ", "author": "Douglas G. Flemons", "genre": "Psychology", "isbn": "3545X "},
{"name": "The Hidden Story Of Every Person", "author": "Robert Pantano", "genre": "Short Stories", "isbn": "70653"},
{"name": "AESOP Five Centuries of Illustrated Fables", "author": "Aesop", "genre": "Fables", "isbn": "00000"}])

get_record = db.books.find({"genre": "Psychology"})
get_record2 = db.books.find({"genre": "Fairytale and Folklore"})
get_record3 = db.books.find({"genre": "Fables"})
print(dumps(get_record, indent=2))
print(dumps(get_record2, indent=2))
print(dumps(get_record3, indent=2))



