import unittest
from unittest.mock import Mock
from services.user_service import UserService

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
