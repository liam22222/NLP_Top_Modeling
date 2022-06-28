from pymongo import MongoClient

def mongo_to_list(collection):

    if __name__ == collection:
        client = MongoClient("localhost", 27017, maxPoolSize=50)
        db = client.localhost
        collection = db['chain']
        cursor = collection.find({})
        return cursor

