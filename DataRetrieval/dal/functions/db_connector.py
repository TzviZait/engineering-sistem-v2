from pymongo import MongoClient





class Conector():
    def __init__(self):
        self.addres = "mongodb://localhost:27017"
        self.db_name = "tweets"

    def DBconnect(self):
        self.client = MongoClient(self.addres)
        self.db = self.client[self.db_name]

    def close(self):
        self.client.close()
        self.db = None
        self.collection = None