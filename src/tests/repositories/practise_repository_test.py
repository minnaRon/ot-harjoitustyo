import unittest
from entities.practise import PracticedWordPair
from repositories.practise_repository import practise_repository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        practise_repository.delete_all()
        practise_repository.create_practiced_pair(3, PracticedWordPair('', '', 1, 2, 3, 5))
        practise_repository.create_practiced_pair(3, PracticedWordPair('', '', 2, 3, 3, 10))
        practise_repository.create_practiced_pair(4, PracticedWordPair('', '', 3, 4, 4, 15))

    def test_using_person_id_practised_pairs_are_found_from_database(self):
        practices = practise_repository.get_practices(3)
        self.assertEqual(len(practices), 2)
    
    def test_save_points_updates_points(self):
        practices = practise_repository.get_practices(3)
        practices[2].points_left = 12
        practise_repository.save_points(practices[2])
        practices = practise_repository.get_practices(3)
        self.assertEqual(practices[2].points_left, 12)
