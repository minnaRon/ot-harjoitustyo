from repositories.practise_repository import (
    practise_repository as default_practise_repository
)
from services.user_service import (
    user_service as default_user_service
)
class PractiseLoginService:
    """Class keeps track of the training progress of the logged-in user."""

    def __init__(self, practise_repository=default_practise_repository,
            user_service=default_user_service
        ):
        """Constructor

        Args:
            practise_repository (class):    Defaults to default_practise_repository.
            user_service (class):           Defaults to default_user_service.

        Other object variables:
            self.words_chosen_to_practise (list):      all pair of words chosen to practise
                                                        (index of pair of words concerns this list)
            self._already_practised (dict):             pair of words which learning progress
                                                        were already saved to the database.
            self.indexes_buttons_word_orig (list):     indexes of pair of original words placed
                                                        to buttons user to see at present.
            self._counter (int):                        counts all clicks of buttons containing word
                                                        during training.
        """
        self._practise_repository = practise_repository
        self._user_service = user_service
        self.words_chosen_to_practise = None
        self.indexes_buttons_word_orig = None
        self._already_practised = None
        self._counter = 0


    def prepare_chosen_words_including_progress(
        self, words_chosen_to_practise, indexes_buttons_word_orig
        ):
        """Connects the progress of the training to a pair of words.

        Calls to remove already learned.

        Args:
            words_chosen_to_practise (list):    all words chosen to practise
            indexes_buttons_word_orig (list):   current indexes of original words in buttons

        Returns:
            list:   all words chosen to practise without already practised
                    containing training progress
        """
        self.words_chosen_to_practise = words_chosen_to_practise
        self.indexes_buttons_word_orig = indexes_buttons_word_orig
        user = self._user_service.get_current_user()
        self._already_practised = self._practise_repository.get_practices(user.id)
        self._counter = 0

        self._remove_already_learned_words()

        for pair in self.words_chosen_to_practise:

            if pair.translation_id in self._already_practised.keys():
                pair.id = self._already_practised[pair.translation_id].id
                pair.person_id = self._already_practised[pair.translation_id].person_id
                pair.points_left = self._already_practised[pair.translation_id].points_left
                pair.new = False

        return self.words_chosen_to_practise

    def add_new_word_index_to_button_word_orig_indexes_depending_on_progress(
        self, biggest_index, indexes_buttons_word_orig
        ):
        """Adds index of new word to button depending of progress of learning.

        Args:
            biggest_index (int):    biggest index of word in buttons so far
            indexes_buttons_word_orig (list):   current indexes of original words in buttons
        """
        self.indexes_buttons_word_orig = indexes_buttons_word_orig
        biggest_i_with_points_left = self._check_next_i_with_points_left(biggest_index+1)
        self.indexes_buttons_word_orig.append((biggest_i_with_points_left))
        self._add_counter_reading_for_progress(biggest_index + 1)


    def _check_next_i_with_points_left(self, next_i):
        """Returns next word index having still learning points to learn.

        Args:
            next_i (int): biggest index of word in buttons so far + 1

        Returns:
            int: next index of word to practice, if no more words to practice, returns -1
        """
        for i in range(next_i,len(self.words_chosen_to_practise)):

            if self.words_chosen_to_practise[i].points_left > 0:
                return i

        return -1


    def _remove_already_learned_words(self):
        """Removes already learned words from chosen words."""
        already_learned = set()

        for pair in self.words_chosen_to_practise:
            if (pair.translation_id in self._already_practised.keys()
                and self._already_practised[pair.translation_id].points_left == 0):

                already_learned.add(pair)

        self.words_chosen_to_practise = list(
            filter(lambda pair : pair not in already_learned, self.words_chosen_to_practise)
            )


    def subtract_points(self, word_i):
        """Updates learning progress to pair of words.

        Correct pair of words subtracts learning points.

        Args:
            word_i (int):   index of pair of words in chosen words
        """
        practiced_pair = self.words_chosen_to_practise[word_i]
        clicks_before_answer = self._counter - practiced_pair.counter_start

        practiced_pair.points_left -= (5 - clicks_before_answer)

        practiced_pair.points_left = max(0, practiced_pair.points_left)
        practiced_pair.points_left = min(15, practiced_pair.points_left)

        self._counter += 1


    def add_points(self, word_i):
        """Updates learning progress to pair of words.

        Incorrect pair of words adds learning points.

        Args:
            word_i (int):   index of pair of words in chosen words
        """
        practiced_pair = self.words_chosen_to_practise[word_i]

        practiced_pair.points_left += 5

        practiced_pair.points_left = min(15, practiced_pair.points_left)

        self._counter += 1


    def _add_counter_reading_for_progress(self, word_i):
        """Adds the start value of the counter to new pair of words to practise.

        Args:
            word_i (int):   index of pair of words in chosen words
        """
        practiced_pair = self.words_chosen_to_practise[word_i]
        practiced_pair.counter_start = self._counter +1


    def save_points(self, words):
        """Calls repository to save learning progress

        If practised pair of words is new creates practiced pair with learning points
        Else updates learning points of pair of words to database.
        """
        user = self._user_service.get_current_user()
        self.words_chosen_to_practise = words
        if user:

            for i in range(0, self._counter+5):

                if self.words_chosen_to_practise[i].new:
                    self._practise_repository.create_practiced_pair(
                        user.id, self.words_chosen_to_practise[i]
                        )

                else:
                    self._practise_repository.save_points(self.words_chosen_to_practise[i])


practise_login_service = PractiseLoginService()
