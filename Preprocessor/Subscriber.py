import datetime
import json
from Tools.TextTools.cleaner import Cleaner
from Tools.kafkaTools.kafakaPusher import Push_kafka
from kafka import KafkaConsumer


class CleanerSubscriber:

    def __init__(self,kafka_address,topic_name,target_topic_name,):
        self.kafka_pusher = Push_kafka(kafka_address)
        self.kafka_pusher.connect()

        self.consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=kafka_address,
            auto_offset_reset='earliest',  
            group_id='my-group'
        )

        for message in self.consumer:
            message = json.loads(message.value.decode('utf-8'))
            cleanData = Cleaner.cleanData(message['text'])
            message['clieanText'] = str(cleanData)
            self.kafka_pusher.send_by_topic_name(target_topic_name,message)