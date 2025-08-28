import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger_eng')


class Lemmatization:

   @staticmethod
   def lemmatization(data):
        lemmatized_words = ""
        lemmatizer = WordNetLemmatizer()

        tokens = word_tokenize(data)
        for word in tokens:
            lemmatized_words += f"{lemmatizer.lemmatize(word)} "

        return lemmatized_words

