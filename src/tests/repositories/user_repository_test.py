import unittest
from repositories.user_repository import user_repository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        user_repository.create('given_username', 'given_password')
    
    def test_method_create_saves_new_user(self):
        user = user_repository.find_by_username('given_username')

        self.assertEqual(user.name, 'given_username' )
    
    def test_method_find_by_username_finds_user(self):
        user_repository.create('other_username', 'given_password2')
        user = user_repository.find_by_username('other_username')

        self.assertEqual(user.name, 'other_username' )

    def test_method_find_by_username_with_no_username_in_database_returns_none(self):
        user = user_repository.find_by_username('not_given_username')

        self.assertEqual(user, None)
