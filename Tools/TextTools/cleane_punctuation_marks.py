import string


class Cleane_punctuation_marks:

    @staticmethod
    def cleane_punctuation_marks(data):

        # Create translation table
        translator = str.maketrans('', '', string.punctuation)

        # Remove punctuation
        clean_text = data.translate(translator)
        return clean_text

