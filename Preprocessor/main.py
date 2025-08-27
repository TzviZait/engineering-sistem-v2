from Preprocessor.Subscriber import CleanerSubscriber



if __name__ == "__main__":
    antisemitic = CleanerSubscriber("localhost:9092","raw_tweets_antisemitic",'preprocessed_tweets_antisemitic')
    # antisemitic = CleanerSubscriber("localhost:9092","interesting",'preprocessed_tweets_antisemitic')
    not_antisemitic = CleanerSubscriber("localhost:9092","raw_tweets_not_antisemitic",'preprocessed_tweets_not_antisemitic')
    # not_antisemitic = CleanerSubscriber("localhost:9092","not_interesting",'preprocessed_tweets_not_antisemitic')