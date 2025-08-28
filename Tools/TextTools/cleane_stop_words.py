
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Cleane_stop_words:

    @staticmethod
    def cleane_stop_words(data):
        data = data.split()
        stopwords.words('english')
        filtered_words = ""
        for word in data:
            if word not in stopwords.words('english'):
                filtered_words += f"{word} "
        return filtered_words
