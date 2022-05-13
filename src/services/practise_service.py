from random import shuffle
from entities.practise import PracticedWordPair
from repositories.practise_repository import (
    practise_repository as default_practise_repository
)
from services.user_service import (
    user_service as default_user_service
)
from services.practise_login_service import (
    practise_login_service as default_practise_login_service
)
class PractiseService:
    """Class takes care of practicing words with translations."""

    def __init__(self, practise_repository=default_practise_repository,
                user_service=default_user_service,
                practise_login_service=default_practise_login_service
                ):
        """Constructor

        Args:
            practise_repository (class):    Defaults to default_practise_repository.
            user_service (class):           Defaults to default_user_service.
            practise_login_service (class): Defaults to default_practise_login_service

        Other object variables:
            self.words_chosen_to_practise (list):      all pair of words chosen to practise
                                                        (index of pair of words concerns this list)
            self.indexes_buttons_word_orig (list):     indexes of pair of original words placed
                                                        to buttons user to see at present.
            self._indexes_buttons_word_transl (list):   indexes of pair of translation words placed
                                                        to buttons user to see at present.
            self._first_clicked_word_i (int):           holds index of first clicked pair of words.
            self._response (string):                    holds message to show in practice_view.
                                                        during training.
        """
        self._practise_repository = practise_repository
        self._practise_login_service = practise_login_service
        self._user_service = user_service
        self.words_chosen_to_practise = None
        self.indexes_buttons_word_orig = None
        self._indexes_buttons_word_transl = None
        self._first_clicked_word_i = None
        self._response = None


    def get_response(self):
        return self._response


    def get_words_to_practise(self):
        return self.words_chosen_to_practise


    def get_word_orig_indexes(self):
        return self.indexes_buttons_word_orig


    def get_word_transl_indexes(self):
        return self._indexes_buttons_word_transl

    def set_words_to_practise(self, lang_orig, lang_transl):
        """Initially sets first pair of words to practice_view of ui.

        Args:
            lang_orig (string):     original language
            lang_transl (string):   translation language
        """
        user = self._user_service.get_current_user()
        self.words_chosen_to_practise = (
            self._practise_repository.get_words_with_translations(lang_orig, lang_transl
        ))
        self.words_chosen_to_practise += [PracticedWordPair('*'*5, '*'*5, None) for i in range(7)]

        if user:
            self.words_chosen_to_practise = (
                self._practise_login_service.prepare_chosen_words_including_progress(
                    self.words_chosen_to_practise, self.indexes_buttons_word_orig
                ))

        if len(self.words_chosen_to_practise) > 7:
            self._prepare_button_word_indexes()

        else:
            self._prepare_button_word_indexes()
            self._response = '''Harjoiteltavien sanojen määrä liian pieni,
                                valitse lisää harjoiteltavia sanoja'''


    def _prepare_button_word_indexes(self):
        """Creates first lists for ui buttons containing word indexes"""
        self.indexes_buttons_word_orig = [0, 1, 2, 3, 4]
        self._indexes_buttons_word_transl = self.indexes_buttons_word_orig[:]
        shuffle(self._indexes_buttons_word_transl)


    def check_word_pair(self, button_index):
        """Handles clicked button of practiced word.

            If clicked button was first and button of origins, sets first selected word index
            If clicked button was second and button of transl, checks correctness of pair of words.
            Else ui response with message to select origin word first.
        Args:
            button_index (int):     index of button clicked
        """
        buttons_biggest_word_index_now = max(self.indexes_buttons_word_orig)

        if self._words_to_practise_still_left(buttons_biggest_word_index_now) == 2:
            self._response = 'HIENOA! Osasit kaikki sanat!'
        else:
            if self._get_word_i_of_button_word(button_index)<=len(self.words_chosen_to_practise)-4:

                if button_index < 5:
                    self._set_first_selected_word_index(button_index)

                elif self._first_clicked_word_i is not None and button_index >= 5:
                    second_clicked_word_index = self._get_word_i_of_button_word(button_index)
                    self._check_correctness_of_pair(second_clicked_word_index)

                else:
                    self._first_clicked_word_i = None
                    self._response = 'valitse ensin yksi sana vasemmalta'

            else:
                self._response = '''Harjoiteltavien sanojen määrä liian pieni,
                                    valitse lisää harjoiteltavia sanoja'''



    def _set_first_selected_word_index(self, button_index):
        """Sets in the object variable the index of the first clicked word.

        Args:
            button_index (int):     index of button clicked
        """
        word_index = self.indexes_buttons_word_orig[button_index]
        self._first_clicked_word_i = word_index
        self._response = None


    def _get_word_i_of_button_word(self, button_index):
        return self._indexes_buttons_word_transl[button_index-5]


    def _check_correctness_of_pair(self, word_i):
        """Checks if buttons clicked contains pair of words.

        If pair of words founded, calls method to handle correct pair.
        Else calls method to handle incorrect pair.

        Args:
            word_i (int):   second clicked button contained index of word
        """

        if self._first_clicked_word_i == word_i:
            self._act_as_pair_correct(word_i)

        else:
            self._act_as_pair_not_correct(word_i)

        self._first_clicked_word_i = None


    def _act_as_pair_correct(self, word_i):
        """Handles correct pair of words.

        If user login, updates learning progress.
        Sets response message 'pari' in object variable.
        Calls method to change new word index in buttons orig and translate.

        Args:
            word_i (int):   index of word second clicked button contained
        """
        user = self._user_service.get_current_user()

        if user:
            self._practise_login_service.subtract_points(word_i)

        self._response = 'pari!'
        self._change_button_word_indexes(word_i)


    def _change_button_word_indexes(self, learned_word_i):
        """Changes new word index in buttons orig and translate.

        If new words to practice still left, changes index of new pair of words to buttons.
        Else sets response message in object variable.

        Args:
            learned_word_i (int):   index of learned word pair in chosen words
        """
        user = self._user_service.get_current_user()
        buttons_biggest_word_index_now = max(self.indexes_buttons_word_orig)

        if self._words_to_practise_still_left(buttons_biggest_word_index_now) == 3:
            self._response = 'HIENOA! Osasit kaikki sanat!'

        self._remove_learned_word_i_from_button_word_indexes(learned_word_i)

        if user:
            (
            self._practise_login_service
                .add_new_word_index_to_button_word_orig_indexes_depending_on_progress(
                    buttons_biggest_word_index_now, self.indexes_buttons_word_orig
                ))
        else:
            self.indexes_buttons_word_orig.append((buttons_biggest_word_index_now +1))

        self._prepare_translation_word_indexes_for_buttons()


    def _words_to_practise_still_left(self, buttons_biggest_word_index_now):
        """Returns True or False regarding is there words still left to practise.

        Args:
            buttons_biggest_word_index_now (int):   biggest index of words practised so far.

        Returns:
            boolean: True is still words left, else False
        """
        return len(self.words_chosen_to_practise) - (buttons_biggest_word_index_now + 1)


    def _remove_learned_word_i_from_button_word_indexes(self, learned_word_i):
        """Removes index of learned pair of words from buttons.

        Args:
            learned_word_i (int):   index of learned word in chosen words to practice
        """
        self.indexes_buttons_word_orig.remove(learned_word_i)

    def _prepare_translation_word_indexes_for_buttons(self):
        """Sets list of indexes of words for translation buttons in ui"""
        self._indexes_buttons_word_transl = self.indexes_buttons_word_orig[:]
        shuffle(self._indexes_buttons_word_transl)


    def _act_as_pair_not_correct(self, word_i):
        """Handles incorrect pair of words.

        If user logged in, updates learning progress points.
        Sets response message in object variable.

        Args:
            word_i (int):   index of word second clicked button contained
        """
        user = self._user_service.get_current_user()

        if user:
            self._practise_login_service.add_points(word_i)

        self._response = 'huti!'

practise_service = PractiseService()
