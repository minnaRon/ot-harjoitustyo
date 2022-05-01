import unittest
from unittest.mock import Mock
from services.user_service import UserService, CredentialsError
from entities.person import Person

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_repo_mock = Mock()
        self.user_service = UserService(self.user_repo_mock)
 
    def test_register_asks_if_user_exists(self):
        self.user_repo_mock.find_by_username.return_value = None
        self.user_service.register('name', 'password')
        self.user_repo_mock.find_by_username.assert_called()

    def test_calls_repo_to_create_user_if_user_not_exist(self):
        self.user_repo_mock.find_by_username.return_value = None
        self.user_service.register('name', 'password')
        self.user_repo_mock.create.assert_called()
    
    def test_register_with_username_in_database__raises_credentialserror(self):
        self.user_repo_mock.find_by_username.return_value = Person('1', 'user_exists', 'password')
        self.assertRaises(CredentialsError, self.user_service.register, 'user_exists', 'password')

    def test_method_logout_removes_user(self):
        self.user_service.logout()
        self.assertEqual(self.user_service._user, None)
    
    def test_login_with_username_in_database__user_is_placed_to_varable(self):
        self.user_repo_mock.find_by_username.return_value = Person('1', 'user_exists', 'password')
        self.user_service.login('user_exists', 'password')
        self.assertEqual(self.user_service._user.name, 'user_exists')
    
    def test_login_with_username_not_in_database__raises_credentialserror(self):
        self.user_repo_mock.find_by_username.return_value = None
        self.assertRaises(CredentialsError, self.user_service.login, 'user_not_exists', 'password')

