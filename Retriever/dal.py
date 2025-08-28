import os

from dotenv import load_dotenv

from pymongo import MongoClient
load_dotenv()

USER = os.getenv("USER")
PASS = os.getenv("PASS")


class DAL:

    def __init__(self):

        self.CONNECTION_STRING = f"mongodb+srv://{USER}:{PASS}@cluster0.6ycjkak.mongodb.net/"

    def get_database(self,skip = 0):

        client = MongoClient(self.CONNECTION_STRING)

        client =  client['IranMalDB']

        collection = client['tweets']

        query = collection.find({},{"_id":0}).sort('CreateDate',1).skip(skip).limit(100)

        return query




