import datetime
import json
from Tools.kafkaTools.kafakaPusher import Push_kafka
from Enricher.processeser import ProcesseData
from kafka import KafkaConsumer


class EnricherSubscriber:

    def __init__(self,kafka_address,topic_name,target_topic_name,):
        self.kafka_pusher = Push_kafka(kafka_address)
        self.kafka_pusher.connect()

        self.consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=kafka_address,
            auto_offset_reset='earliest',  
            group_id='my-group'
        )
        i = 0
        for message in self.consumer:
            message = json.loads(message.value.decode('utf-8'))
            addFilds = ProcesseData.processing(message)
            for fild in addFilds.keys():
                message[fild] = addFilds[fild]
            self.kafka_pusher.send_by_topic_name(target_topic_name,message)
            print(F"messeage {i} sended")
            i += 1