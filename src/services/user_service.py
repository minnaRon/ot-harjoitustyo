from repositories.user_repository import (
    user_repository as default_user_repository
)
class CredentialsError(Exception):
    pass

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository
        self._user = None


    def register(self, username, password1=None):

        user_exists = self._user_repository.find_by_username(username)

        if user_exists:
            raise CredentialsError('tunnus on jo käytössä')

        self._user = self._user_repository.create(username, password1)


    def login(self, username, password):

        user = self._user_repository.find_by_username(username)

        if user and (not user.password or user.password == password):
            self._user = user

        else:
            raise CredentialsError('tunnus tai salasana virheellinen')


    def logout(self):
        self._user = None


    def get_current_user(self):
        return self._user


user_service = UserService()
