import unittest
from unittest.mock import Mock
from services.practise_login_service import PractiseLoginService
from entities.practise import PracticedWordPair
from entities.person import Person

class TestPractiseLoginService(unittest.TestCase):
    def setUp(self):
        self.user_service_mock = Mock()
        self.practise_repo_mock = Mock()
        self.practise_login_service = PractiseLoginService(self.practise_repo_mock, self.user_service_mock)
        self.user_service_mock.get_current_user.return_value = Person(1, 'given_username','given_password')
        self.practise_repo_mock.get_practices.return_value = {1:PracticedWordPair("", "", 1, 2, 1, 15)}
        words_chosen = (PracticedWordPair('sana0','word0',0),PracticedWordPair('sana1','word1',1))
        self.practise_login_service.prepare_chosen_words_including_progress(words_chosen, [0, 1, 2, 3, 4])
        
    def test_initially_counter_0(self):
        self.assertEqual(self.practise_login_service._counter, 0)

    def test_two_pairs_with_right_info__when_setup_pair_of_words_given_(self):
        self.assertEqual(len(self.practise_login_service.words_chosen_to_practise),2)
        self.assertEqual(self.practise_login_service.words_chosen_to_practise[0].points_left, 5)
        self.assertEqual(self.practise_login_service.words_chosen_to_practise[1].points_left, 15)
        self.assertEqual(self.practise_login_service.words_chosen_to_practise[0].new, True)
        self.assertEqual(self.practise_login_service.words_chosen_to_practise[1].new, False)
        self.assertEqual(self.practise_login_service.words_chosen_to_practise[0].translation_id, 0)
        self.assertEqual(self.practise_login_service.words_chosen_to_practise[1].translation_id, 1)
        self.assertEqual(self.practise_login_service.words_chosen_to_practise[1].person_id, 1)
        self.assertEqual(self.practise_login_service.words_chosen_to_practise[0].counter_start, 0)

    def test_remove_already_learned_words(self):
        self.practise_repo_mock.get_practices.return_value = {1:PracticedWordPair("", "", 1, 2, 1, 0)}
        words_chosen = (PracticedWordPair('sana0','word0',0),PracticedWordPair('sana1','word1',1))
        self.practise_login_service.prepare_chosen_words_including_progress(words_chosen, [0, 1, 2, 3, 4])
        self.assertEqual(len(self.practise_login_service.words_chosen_to_practise),1)
        self.assertEqual(self.practise_login_service.words_chosen_to_practise[0].points_left, 5)

    def test_subtract_points_adds_already_learned(self):
        self.practise_login_service.subtract_points(0)
        self.assertEqual(len(self.practise_login_service.already_learned),1)

    def test_subtract_points__subtracts_5_points(self):
        self.practise_login_service.subtract_points(1)
        self.assertEqual(self.practise_login_service.words_chosen_to_practise[1].points_left, 10)

    def test_add_points__adds_5_points(self):
        self.practise_login_service.add_points(0)
        self.assertEqual(self.practise_login_service.words_chosen_to_practise[0].points_left, 10)
    
    def test_add_points__not_add_if_already_15_points(self):
        self.practise_login_service.add_points(1)
        self.assertEqual(self.practise_login_service.words_chosen_to_practise[1].points_left, 15)
    
    def test_save_points__calls_repo_to_save(self):
        self.practise_login_service.save_points(self.practise_login_service.words_chosen_to_practise)
        self.practise_repo_mock.save_points.assert_called()
