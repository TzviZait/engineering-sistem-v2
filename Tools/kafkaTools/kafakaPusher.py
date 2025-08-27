from kafka import KafkaProducer
import json



class Push_kafka:

    def __init__(self,addres:str)->None:
        self.addres = addres
    
    def connect(self)->None:
        self.producer = KafkaProducer(bootstrap_servers = self.addres)

    def send_by_topic_name(self,topicName:str,message:dict)->None:
        self.producer.send(topicName,json.dumps(message).encode('utf-8'))

    def close(self)->None:
        self.producer.close()
