from random import shuffle

class PractiseService:
    def __init__(self):
        self._words_chosen_to_practise = None
        self._indexes_buttons_word_orig = None
        self._indexes_buttons_word_transl = None
        self._first_clicked_word_i = None
        self._response = None

    def get_response(self):
        return self._response

    def get_words_to_practise(self):
        return self._words_chosen_to_practise

    def get_word_orig_indexes(self):
        return self._indexes_buttons_word_orig

    def get_word_transl_indexes(self):
        return self._indexes_buttons_word_transl

    def check_pair(self, word_i):
        if self._first_clicked_word_i == word_i:
            self._first_clicked_word_i = None
            self._response = 'pari!'
            self._change_button_word_indexes(word_i)
        else:
            self._first_clicked_word_i = None
            self._response = 'huti!'

    def _change_button_word_indexes(self, learned_word_i):
        biggest_index = max(self._indexes_buttons_word_orig)

        if biggest_index < len(self._words_chosen_to_practise) -5:

            self._indexes_buttons_word_orig.remove(learned_word_i)
            self._indexes_buttons_word_transl.remove(learned_word_i)

            self._indexes_buttons_word_orig.append((biggest_index + 1))
            self._indexes_buttons_word_transl = self._indexes_buttons_word_orig[:]
            shuffle(self._indexes_buttons_word_transl)

        else:
            self._response = '''HIENOA! Olet osannut kaikki sanat kerran!
                             Jos haluat harjoitella sanoja tehokkaammin, 
                             kirjautuneena saat kaikki sovelluksen ominaisuudet
                              käyttöösi.'''

    #sanat kovakoodattu kunnes tietokanta mukana
    def _set_words_to_practise(self, lang_orig, lang_transl):
        self._words_chosen_to_practise = [('sana1', 'word1'), ('sana2', 'word2'),
            ('sana3', 'word3'), ('sana4', 'word4'), ('sana5', 'word5'), ('sana6', 'word6'),
            ('sana7', 'word7'), ('sana8', 'word8'), ('sana9', 'word9'), ('sana10', 'word10'),
            ('sana11', 'word11'), ('sana12', 'word12'), ('sana13', 'word13'), ('sana14', 'word14'),
            ('sana15', 'word15'), ('sana16', 'word16'), ('sana17', 'word17'), ('sana18', 'word18'),
            ('sana19', 'word19'), ('sana20', 'word20'), ('sana21', 'word21'), ('sana22', 'word22'),
            ('sana23', 'word23'), ('sana24', 'word24'), ('sana225', 'word25'), ('sana26', 'word26'),
            ('sana27', 'word27'), ('sana28', 'word28')]

        if len(self._words_chosen_to_practise) > 5:
            self._indexes_buttons_word_orig = [0, 1, 2, 3, 4]
            self._indexes_buttons_word_transl = self._indexes_buttons_word_orig[:]
            shuffle(self._indexes_buttons_word_transl)

        else:
            self._response = '''Harjoiteltavien sanojen määrä liian pieni,
                                valitse lisää harjoiteltavia sanoja'''

    def set_clicked_word_index(self, word_i):
        self._first_clicked_word_i = word_i

    def check_word_pair(self, button_index):

        if self._first_clicked_word_i is None and button_index <5:
            word_index = self._indexes_buttons_word_orig[button_index]
            self._first_clicked_word_i = word_index

        elif self._first_clicked_word_i is not None and button_index >= 5:
            word_index = self._indexes_buttons_word_transl[button_index-5]
            self.check_pair(word_index)
        else:
            self._first_clicked_word_i = None
            self._response = 'valitse ensin yksi sana vasemmalta'


practise_service = PractiseService()
