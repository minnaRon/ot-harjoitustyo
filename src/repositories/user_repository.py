from database_connection import get_database_connection
from entities.person import Person

class UserRepository:
    """Class takes care of database operations related to user."""

    def __init__(self, connection):
        """Constructor creates database connection

        Args:
            connection (object):    object of database connection
        """
        self.__connection = connection


    def create(self, username, password=None):
        """Creates new user in database.

        Args:
            username (string):  user name
            password (string):  user password

        Returns:
            object Person:  object contains user id, username, password
        """
        cursor = self.__connection.cursor()
        cursor.execute('''
            INSERT INTO Persons (name, password) 
            VALUES (?,?)
            ''', [username, password]
            )
        self.__connection.commit()

        person_id = cursor.lastrowid

        return Person(person_id, username, password)


    def find_by_username(self, username):
        """Returns Person object where username is as asked.

        Args:
            username (string):  user username

        Returns:
            object Person:  contains user id, username, password
        """
        cursor = self.__connection.cursor()

        cursor.execute('''
            SELECT id, name, password 
            FROM Persons
            WHERE name=?
            ''', [username]
        )

        row = cursor.fetchone()

        if row:
            return Person(row[0], row[1], row[2])

        return None


    def delete_all(self):
        """Deletes all from table Persons"""
        cursor = self.__connection.cursor()

        cursor.execute('DELETE FROM Persons')

        self.__connection.commit()


user_repository = UserRepository(get_database_connection())
