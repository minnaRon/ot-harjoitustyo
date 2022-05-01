import unittest
from services.practise_service import PractiseService

class FakePractiseRepository:
    def __init__(self, connection=None):
        self.words = []

    def get_words_with_translations(self, lang_orig, lang_transl):
        for i in range(1, 10+1):
            self.words += ("sana"+str(i), "word"+str(i))
        return self.words


class TestPractiseService(unittest.TestCase):
    def setUp(self):
        self.service = PractiseService(FakePractiseRepository())
        self.service.set_words_to_practise('English', 'Finnish')
        self.service._indexes_buttons_word_orig = [0, 1, 2, 3, 4]
        self.service._indexes_buttons_word_transl = [1, 2, 3, 4, 5]

    def test_method_set_words_created_list_with_words(self):
        self.assertTrue(self.service._words_chosen_to_practise)

    def test_when_words_are_pair_then_string_pari_in_response_variable(self):
        self.service._first_clicked_word_i = 2
        self.service._check_correctness_of_pair(2)
        self.assertEqual(self.service._response, 'pari!')

    def test_when_words_not_pair_then_string_huti_in_response_variable(self):
        self.service._first_clicked_word_i = 2
        self.service._check_correctness_of_pair(1)
        self.assertEqual(self.service._response, 'huti!')

    def test_first_clicked_word_is_saved_in_variable(self):
        self.service.check_word_pair(3)
        self.assertEqual(self.service._first_clicked_word_i, 3)

    def test_valid_second_clicked_word_calls_method_to_check_pair(self):
        self.service._first_clicked_word_i = 2
        self.service.check_word_pair(6)
        self.assertEqual(self.service._response, 'pari!')

    def test_not_valid_second_clicked_word__gives_response(self):
        self.service._first_clicked_word_i = 2
        self.service.check_word_pair(3)
        self.assertNotEqual(self.service._response, None)
        