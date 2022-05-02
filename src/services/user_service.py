from repositories.user_repository import (
    user_repository as default_user_repository
)
class CredentialsError(Exception):
    pass

class UserService:
    """Class takes care of user operations."""

    def __init__(self, user_repository=default_user_repository):
        """Constructor

        Args:
            user_repository (class):    Defaults to default_user_repository.

        Other object variables:
            self._user (object Person): holds person of user if logged in.
        """
        self._user_repository = user_repository
        self._user = None


    def register(self, username, password1=None):
        """Calls repository to create user.

        Args:
            username (string):  user username
            password1 (string): user password if given

        Raises:
            CredentialsError:   if username already exists
        """
        user_exists = self._user_repository.find_by_username(username)

        if user_exists:
            raise CredentialsError('tunnus on jo käytössä')

        self._user = self._user_repository.create(username, password1)


    def login(self, username, password):
        """Logs user in if username and password are correct.

        Args:
            username (string):  user username
            password (string):  user password

        Raises:
            CredentialsError:   if incorrect username or password
        """
        user = self._user_repository.find_by_username(username)

        if user and (not user.password or user.password == password):
            self._user = user

        else:
            raise CredentialsError('tunnus tai salasana virheellinen')


    def logout(self):
        """if user is logged in logs user out."""
        self._user = None


    def get_current_user(self):
        return self._user


user_service = UserService()
