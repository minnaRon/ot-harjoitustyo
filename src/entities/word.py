class Word:
    """Class for word info."""
    def __init__(self, word, language):
        """Constructor creates word with related information.

        Args:
            word (string):      word
            language (string):  language of the word
        """
        self.id = None
        self.word = word
        self.language = language
