import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')


class Classification:

    @staticmethod
    def get_comp_level(comp)->str:
        if 0.5<= comp <=1:
            return "positive"
        if -0.5 < comp < 0.5:
            return "neutral"
        if -0.5 >= comp >-1:
            return "negative"
        

    @staticmethod  
    def get_compound(tweet:str) -> str:
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        return Classification.get_comp_level(score['compound'])
    
# print(Classification.get_compound('sdsanddunes barbarian kkk nazi isi wirathu jvp zionazis hadhave constituent open closeted'))