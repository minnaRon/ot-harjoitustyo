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
        self.service._set_words_to_practise('English', 'Finnish')

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
