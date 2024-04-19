from pymongo import MongoClient, errors
from bson.json_util import dumps
import os


MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/sample_restaurants"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
db = client.zgb8ts
coll = db.books