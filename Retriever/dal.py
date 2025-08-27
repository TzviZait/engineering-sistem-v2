import time
from datetime import date, datetime

import schedule
import pymongo

from pymongo import MongoClient

class DAL:

    def __init__(self):
        self.CONNECTION_STRING = "mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/"

    def get_database(self):

        client = MongoClient(self.CONNECTION_STRING)

        client =  client['IranMalDB']

        collection = client['tweets']

        query = collection.find({},{"_id":0}).limit(50)

        return query




