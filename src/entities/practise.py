class Practice:
    def __init__(
                self, word_orig, word_transl, translation_id,
                id=None, person_id=None, points_left=5
        ):
        self.id = id
        self.person_id = person_id
        self.translation_id = translation_id
        self.word_orig = word_orig
        self.word_transl = word_transl
        self.points_left = points_left
        self.counter_start = 0
        self.new = True
