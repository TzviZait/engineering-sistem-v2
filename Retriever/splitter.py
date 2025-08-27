
from Tools.kafkaTools.kafakaPusher import Push_kafka

class Splitter:
    def __init__(self):
        self.pusher = Push_kafka("localhost:9092")


    def splitter(self,data):
        self.pusher.connect()

        for message in data:
            message['CreateDate'] = message['CreateDate'].isoformat()
            print(message)
            if message['Antisemitic']:
                self.pusher.send_by_topic_name('raw_tweets_antisemitic',message)

            else:
                self.pusher.send_by_topic_name('raw_tweets_not_antisemitic',message)
        self.pusher.close()

