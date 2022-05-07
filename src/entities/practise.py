class PracticedWordPair:
    """Class to maintain information of learning progress of pair of words."""

    def __init__(
                self, word_orig, word_transl, translation_id,
                id=None, person_id=None, points_left=5
        ):
        """Constructor creates learning information for pair of words.

        Args:
            word_orig (string):     original word
            word_transl (string):   translation of original word
            translation_id (int):   rowid for pair of words from database table Translations
            id (int):               rowid for practiced pair of words info from table Practices
            person_id (int):        rowid for user from database table Persons
            points_left (int):      learning points measures progress of learning

        Other object variables:
            self.counter_start (int):   holds value of start when the pair of words
                                        is visible to the user in the user interface.
                                        (object variable counter is placed in class PracticeService)
            self.new (int):     status of pair of words.
                                If new is True, pair of words is not yet in the database.
        """
        self.id = id
        self.person_id = person_id
        self.translation_id = translation_id
        self.word_orig = word_orig
        self.word_transl = word_transl
        self.points_left = points_left
        self.counter_start = 0
        self.new = True
