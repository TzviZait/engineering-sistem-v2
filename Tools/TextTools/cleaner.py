
from Tools.TextTools.cleane_stop_words import Cleane_stop_words
from Tools.TextTools.convert_text_to_lowercase import Convert_text_to_lowercase
from Tools.TextTools.cleane_unnecessary_whitespace_characters import Cleane_unnecessary_whitespace_characters
from Tools.TextTools.cleane_punctuation_marks import Cleane_punctuation_marks
from Tools.TextTools.lemmatization import Lemmatization
class Cleaner:

    @staticmethod
    def cleanData(data):
        data = Cleane_punctuation_marks.cleane_punctuation_marks(data)
        data = Cleane_unnecessary_whitespace_characters.cleane_unnecessary_whitespace_characters(data)
        data = Cleane_stop_words.cleane_stop_words(data)
        data = Convert_text_to_lowercase.convert_text_to_lowercase(data)
        data = Lemmatization.lemmatization(data)

        return data

