import json
from Tools.kafkaTools.kafakaPusher import Push_kafka
from Enricher.processeser import ProcesseData
from kafka import KafkaConsumer


class EnricherSubscriber:

    def __init__(self,kafka_address,topics_names_1,topics_names_2,target_topic_name_1,target_topic_name_2):
        self.kafka_pusher = Push_kafka(kafka_address)
        self.kafka_pusher.connect()

        self.consumer = KafkaConsumer(
            topics_names_1,topics_names_2,
            bootstrap_servers=kafka_address,
            auto_offset_reset='earliest',  
            group_id='my-group'
        )
        i = 0
        for message in self.consumer:
            message_val = json.loads(message.value.decode('utf-8'))
            print(message_val)
            addFilds = ProcesseData.processing(message_val['text'])
            for fild in addFilds.keys():
                message_val[fild] = addFilds[fild]
            if message.topic == topics_names_1:
                self.kafka_pusher.send_by_topic_name(target_topic_name_1,message_val)
            else:
                self.kafka_pusher.send_by_topic_name(target_topic_name_2,message_val)
            print(F"messeage {i} sended {message.topic}")
            i += 1