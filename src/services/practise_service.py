from random import shuffle
from repositories.practise_repository import (
    practise_repository as default_practise_repository
)
from services.user_service import (
    user_service as default_user_service
)

class PractiseService:
    def __init__(self, practise_repository=default_practise_repository,
            user_service=default_user_service
        ):
        self._practise_repository = practise_repository
        self._user_service = user_service
        self._words_chosen_to_practise = None
        self._already_practised = None
        self._indexes_buttons_word_orig = None
        self._indexes_buttons_word_transl = None
        self._first_clicked_word_i = None
        self._user = None
        self._response = None
        self._counter = 0


    def get_response(self):
        return self._response


    def get_words_to_practise(self):
        return self._words_chosen_to_practise


    def get_word_orig_indexes(self):
        return self._indexes_buttons_word_orig


    def get_word_transl_indexes(self):
        return self._indexes_buttons_word_transl

    def set_words_to_practise(self, lang_orig, lang_transl):
        self._user = self._user_service.get_current_user()
        self._counter = 0
        self._words_chosen_to_practise = (
            self._practise_repository.get_words_with_translations(lang_orig, lang_transl
        ))
        if self._user:
            self._prepare_chosen_words_including_progress()

        if len(self._words_chosen_to_practise) > 5:
            self._prepare_button_word_indexes()

        else:
            self._response = '''Harjoiteltavien sanojen määrä liian pieni,
                                valitse lisää harjoiteltavia sanoja'''


    def _prepare_button_word_indexes(self):
        self._indexes_buttons_word_orig = [0, 1, 2, 3, 4]
        self._indexes_buttons_word_transl = self._indexes_buttons_word_orig[:]
        shuffle(self._indexes_buttons_word_transl)


    def check_word_pair(self, button_index):

        if self._first_clicked_word_i is None and button_index < 5:
            self._set_first_selected_word_index(button_index)

        elif self._first_clicked_word_i is not None and button_index >= 5:
            second_clicked_word_index = self._get_word_i_of_button_word(button_index)
            self._check_correctness_of_pair(second_clicked_word_index)

        else:
            self._first_clicked_word_i = None
            self._response = 'valitse ensin yksi sana vasemmalta'


    def _set_first_selected_word_index(self, button_index):
        word_index = self._indexes_buttons_word_orig[button_index]
        self._first_clicked_word_i = word_index
        # lisaa kun muutkin variablet self._response = None


    def _get_word_i_of_button_word(self, button_index):
        return self._indexes_buttons_word_transl[button_index-5]


    def _check_correctness_of_pair(self, word_i):
        self._user = self._user_service.get_current_user()

        if self._first_clicked_word_i == word_i:
            self._act_as_pair_correct(word_i)

        else:
            self._act_as_pair_not_correct(word_i)

        self._first_clicked_word_i = None
        self._counter += 1


    def _act_as_pair_correct(self, word_i):

        if self._user:
            self._subtract_points(word_i)

        self._response = 'pari!'
        self._change_button_word_indexes(word_i)


    def _change_button_word_indexes(self, learned_word_i):
        self._user = self._user_service.get_current_user()
        buttons_biggest_word_index_now = max(self._indexes_buttons_word_orig)

        if self._words_to_practise_still_left(buttons_biggest_word_index_now):

            self._remove_learned_word_i_from_button_word_indexes(learned_word_i)

            if self._user:
                self._add_new_word_index_to_button_word_orig_indexes_depending_on_progress(
                    buttons_biggest_word_index_now
                    )
            else:
                self._indexes_buttons_word_orig.append((buttons_biggest_word_index_now +1))

            self._prepare_translation_word_indexes_for_buttons()

        else:
            self._response = 'HIENOA! Olet osannut kaikki sanat kerran!'


    def _words_to_practise_still_left(self, buttons_biggest_word_index_now):
        return buttons_biggest_word_index_now < len(self._words_chosen_to_practise) - 5


    def _remove_learned_word_i_from_button_word_indexes(self, learned_word_i):
        self._indexes_buttons_word_orig.remove(learned_word_i)
        self._indexes_buttons_word_transl.remove(learned_word_i)


    def _add_new_word_index_to_button_word_orig_indexes_depending_on_progress(self, biggest_index):
        biggest_i_with_points_left = self._check_next_i_with_points_left(biggest_index+1)
        self._indexes_buttons_word_orig.append((biggest_i_with_points_left))
        self._add_counter_reading_for_progress(biggest_index + 1)


    def _prepare_translation_word_indexes_for_buttons(self):
        self._indexes_buttons_word_transl = self._indexes_buttons_word_orig[:]
        shuffle(self._indexes_buttons_word_transl)


    def _act_as_pair_not_correct(self, word_i):

        if self._user:
            self._add_points(word_i)

        self._response = 'huti!'


    def _check_next_i_with_points_left(self, next_i):

        for i in range(next_i,len(self._words_chosen_to_practise)):

            if self._words_chosen_to_practise[i].points_left > 0:
                return i

        return -1


    def _prepare_chosen_words_including_progress(self):
        self._user = self._user_service.get_current_user()
        self._already_practised = self._practise_repository.get_practices(self._user.id)

        self._remove_already_learned_words()

        for pair in self._words_chosen_to_practise:

            if pair.translation_id in self._already_practised.keys():
                pair.id = self._already_practised[pair.translation_id].id
                pair.person_id = self._already_practised[pair.translation_id].person_id
                pair.points_left = self._already_practised[pair.translation_id].points_left
                pair.new = False


    def _remove_already_learned_words(self):
        already_learned = set()

        for pair in self._words_chosen_to_practise:
            if (pair.translation_id in self._already_practised.keys()
                and self._already_practised[pair.translation_id].points_left == 0):

                already_learned.add(pair)

        self._words_chosen_to_practise = list(
            filter(lambda pair : pair not in already_learned, self._words_chosen_to_practise)
            )


    def _subtract_points(self, word_i):
        practiced_pair = self._words_chosen_to_practise[word_i]
        clicks_before_answer = self._counter - practiced_pair.counter_start

        practiced_pair.points_left -= (5 - clicks_before_answer)

        practiced_pair.points_left = max(0, practiced_pair.points_left)
        practiced_pair.points_left = min(15, practiced_pair.points_left)


    def _add_points(self, word_i):
        practiced_pair = self._words_chosen_to_practise[word_i]

        practiced_pair.points_left += 5

        practiced_pair.points_left = min(15, practiced_pair.points_left)


    def _add_counter_reading_for_progress(self, word_i):
        practiced_pair = self._words_chosen_to_practise[word_i]
        practiced_pair.counter_start = self._counter +1


    def save_points(self):
        self._user = self._user_service.get_current_user()

        if self._user:

            for i in range(0, self._counter+5):

                if self._words_chosen_to_practise[i].new:
                    self._practise_repository.create_practiced_pair(
                        self._user.id, self._words_chosen_to_practise[i]
                        )

                else:
                    self._practise_repository.save_points(self._words_chosen_to_practise[i])

        self._response = None

practise_service = PractiseService()
