from Enricher.Subscriber import EnricherSubscriber



if __name__ == "__main__":
    antisemitic = EnricherSubscriber("localhost:9092","preprocessed_tweets_antisemitic",'preprocessed_tweets_not_antisemitic','enriched_preprocessed_tweets_antisemitic','enriched_preprocessed_tweets_not_antisemitic')
    # not_antisemitic = EnricherSubscriber("localhost:9092","preprocessed_tweets_not_antisemitic",'enriched_preprocessed_tweets_not_antisemitic')
