import pymongo

connStr = "mongodb://localhost27017"
database = "myProjectDB"
client = pymongo.MongoClient(connStr)
db = client[database]
info = db['stocks']   # collection
prices = db["stockPrices"]