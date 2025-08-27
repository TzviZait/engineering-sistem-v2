from kafka import KafkaConsumer

import pymongo

from datetime import datetime

class DAL:
    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = myclient["tweets"]



    def dal(self,colName,data):
        mycol = self.mydb[colName]
             # datetime.now().strftime("%H:%M:%S")
            # my_dict = {datetime.now().strftime("%H:%M:%S"): message.value.decode('utf-8')}
        mycol.insert_one(data)

