import unittest
from entities.practise import PracticedWordPair
from repositories.practise_repository import practise_repository
from repositories.user_repository import user_repository
from services.user_service import user_service 
from services.word_service import word_service
from services.practise_login_service import practise_login_service
from services.practise_service import practise_service
from repositories.word_repository import word_repository


class TestMultiClass(unittest.TestCase):
    def setUp(self):
        self.word_repository = word_repository
        self.user_service = user_service
        self.word_service = word_service
        self.practise_service = practise_service
        self.practise_login_service = practise_login_service
        self.practise_repository = practise_repository
        self.user_repository = user_repository
        self.practise_repository.delete_all()
        self.word_repository.delete_all()
        self.user_repository.delete_all()


    def test_user_saved_and_found_correctly(self):
        self.user_service.register('given_username1', 'given_password1')
        self.user_service.register('given_username2', 'given_password2')
        self.user_service.register('given_username3')
        self.assertFalse(self.user_repository.find_by_username('given_username4'))
        self.assertTrue(self.user_repository.find_by_username('given_username1'))
        self.assertEqual(self.user_repository.find_by_username('given_username1').password, 'given_password1')
        self.assertEqual(self.user_repository.find_by_username('given_username2').password, 'given_password2')
        self.assertTrue(self.user_repository.find_by_username('given_username3'))
        self.assertEqual(self.user_repository.find_by_username('given_username3').password, None)


    def test_words_saved_and_practiced_pair_created_correctly(self):
        self.word_service._add_words(['sana1','sana2','sana3'], 'suomi', ['word1','word2','word3'], 'englanti')
        pairs = self.practise_repository.get_words_with_translations('English', 'Finnish')
        self.assertEqual(len(pairs),3)
        self.assertEqual(pairs[0].word_orig, 'word1')
        self.assertEqual(pairs[2].word_transl, 'sana3')
        self.assertEqual(pairs[0].id, None)
        self.assertEqual(pairs[0].person_id, None)
        self.assertEqual(pairs[1].translation_id, 2)
        self.assertEqual(pairs[0].points_left, 5)
        self.assertEqual(pairs[1].counter_start, 0)
        self.assertEqual(pairs[2].new, True)


    def test_progress_of_practice_saved_correctly_in_database(self):
        self.user_service.register('given_username1', 'given_password1')
        self.word_service._add_words(['sana1','sana2','sana3'], 'suomi', ['word1','word2','word3'], 'englanti')
        self.practise_login_service.words_chosen_to_practise = self.practise_repository.get_words_with_translations('English', 'Finnish')
        self.practise_login_service.words_chosen_to_practise[0].points_left = 15
        self.practise_login_service.words_chosen_to_practise[2].points_left = 0
        self.practise_login_service._counter = 4
        self.practise_login_service.save_points(self.practise_login_service.words_chosen_to_practise)
        practiced_pairs = self.practise_repository.get_practices(1)
        self.assertEqual(len(practiced_pairs),3)
        self.assertEqual(practiced_pairs[1].points_left, 15)
        self.assertEqual(practiced_pairs[2].points_left, 5)
        self.assertEqual(practiced_pairs[3].points_left, 0)


    def test_progress_of_practice_deleted_correctly_from_database(self):    
        self.user_service.register('given_username1', 'given_password1')
        self.word_service._add_words(['sana1','sana2','sana3'], 'suomi', ['word1','word2','word3'], 'englanti')
        self.practise_login_service.words_chosen_to_practise = self.practise_repository.get_words_with_translations('English', 'Finnish')
        self.practise_login_service.words_chosen_to_practise[0].points_left = 15
        self.practise_login_service.words_chosen_to_practise[2].points_left = 0
        self.practise_login_service._counter = 4
        self.practise_login_service.save_points(self.practise_login_service.words_chosen_to_practise)
        practiced_pairs = self.practise_repository.get_practices(1)
        self.assertEqual(len(practiced_pairs),3)
        self.assertEqual(practiced_pairs[1].points_left, 15)
        self.assertEqual(practiced_pairs[2].points_left, 5)
        self.assertEqual(practiced_pairs[3].points_left, 0)
        self.practise_login_service.delete_all_progress()
        
        practiced_pairs = self.practise_repository.get_practices(1)
        self.assertFalse(practiced_pairs)
