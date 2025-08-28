from Persister.Subscriber import Subscriber



if __name__ == "__main__":
    Subscriber("localhost:9092",'enriched_preprocessed_tweets_antisemitic','enriched_preprocessed_tweets_not_antisemitic','tweets_antisemitic','tweets_not_antisemitic')
