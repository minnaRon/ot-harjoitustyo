import unittest
from services.practise_service import PractiseService

class TestPractiseService(unittest.TestCase):
    def setUp(self):
        self.service = PractiseService()
        self.service._set_words_to_practise('finnish', 'english')

    def test_method_set_words_created_list_with_words(self):
        self.assertTrue(self.service._words_chosen_to_practise)

    def test_when_words_are_pair_then_string_pari_in_response_variable(self):
        self.service._first_clicked_word_i = 2
        self.service.check_pair(2)
        self.assertEqual(self.service._response, 'pari!')

    def test_when_words_not_pair_then_string_huti_in_response_variable(self):
        self.service._first_clicked_word_i = 2
        self.service.check_pair(1)
        self.assertEqual(self.service._response, 'huti!')
