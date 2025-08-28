import datetime
import json
from kafka import KafkaConsumer
from Persister.dal import DAL

class Subscriber:

    def __init__(self,kafka_address,topics_names_1,topics_names_2,col_name_1,col_name_2):
        self.dal = DAL()
        self.consumer = KafkaConsumer(
            topics_names_1,topics_names_2,
            bootstrap_servers=kafka_address,
            auto_offset_reset='earliest',  
            group_id='my-group'
        )
        i = 0
        for message in self.consumer:
            message_val = json.loads(message.value.decode('utf-8'))
            if message.topic == topics_names_1:
                self.dal.send(col_name_1,message_val)
            else:
                self.dal.send(col_name_2,message_val)
            print(F"messeage {i} sended {message.topic}")
            i += 1