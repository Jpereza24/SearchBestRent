from pymongo import MongoClient

def connectCollection(database, collection):
    #function to connect with MongoDB database and collection.
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll