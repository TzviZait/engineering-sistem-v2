from Tools.TextTools.cleane_punctuation_marks import Cleane_punctuation_marks


class Cleane_unnecessary_whitespace_characters:

    @staticmethod
    def cleane_unnecessary_whitespace_characters(data):
        data = " ".join(data.split())
        return data

