from random import shuffle
from repositories.practise_repository import (
    practise_repository as default_practise_repository
)


class PractiseService:
    def __init__(self, practise_repository=default_practise_repository):
        self.practise_repository = practise_repository
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

        if biggest_index < len(self._words_chosen_to_practise) - 5:

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

    def _set_words_to_practise(self, lang_orig, lang_transl):
        self._words_chosen_to_practise = self.practise_repository.get_words_with_translations(
            lang_orig, lang_transl
        )

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

        if self._first_clicked_word_i is None and button_index < 5:
            word_index = self._indexes_buttons_word_orig[button_index]
            self._first_clicked_word_i = word_index

        elif self._first_clicked_word_i is not None and button_index >= 5:
            word_index = self._indexes_buttons_word_transl[button_index-5]
            self.check_pair(word_index)
        else:
            self._first_clicked_word_i = None
            self._response = 'valitse ensin yksi sana vasemmalta'


practise_service = PractiseService()
