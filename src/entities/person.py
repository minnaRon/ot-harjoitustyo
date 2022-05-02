class Person:
    """Class for keeping user info."""
    def __init__(self, id, username, password):
        """Constructor creates user.

        Args:
            id (int):           user id same as database table Persons rowid for user
            username (string):  user username
            password (string):  user password
        """
        self.id = id
        self.name = username
        self.password = password
