from database_connection import get_database_connection
from entities.practise import Practice


class PractiseRepository:
    """Class takes care of database operations related to practiced pairs of words."""
    def __init__(self, connection):
        """Constructor creates database connection

        Args:
            connection (object):    object of database connection
        """
        self.__connection = connection


    def get_words_with_translations(self, lang_orig, lang_transl):
        """Returns Practice objects of all pairs of words where languages are as asked.

        Args:
            lang_orig (string):     language of origin word
            lang_transl (string):   language of translation

        Returns:
            object Practice:  object contains origin word, translation, id of word pair
        """
        cursor = self.__connection.cursor()
        cursor.execute('''
                SELECT O.word, T.word, TR.id
                FROM Words O
                JOIN Translations TR ON TR.word_orig_id = O.id
                JOIN Words T ON T.id = TR.word_transl_id
                WHERE O.language = ?
                AND T.language = ?
                ORDER BY length(O.word)
                ''', [lang_orig, lang_transl]
        )
        rows = cursor.fetchall()

        return [Practice(row[0], row[1], row[2]) for row in rows]


    def get_practices(self, person_id):
        """Returns Practice objects where person id is as asked.

        Args:
            person_id (int):    user id

        Returns:
            object Practice:    object contains object id, pair of words id, practicing points left.

        """
        cursor = self.__connection.cursor()
        cursor.execute('''
                SELECT id, translation_id, practicing_points_left
                FROM Practices
                WHERE person_id = ?
                ''', [person_id]
        )
        rows = cursor.fetchall()

        return {row[1]:Practice("", "", row[1], row[0], person_id, row[2]) for row in rows}


    def save_points(self, practice: Practice):
        """Saves learning progress points of user concerning pair of words.

        Args:
            practice (Practice):    object contains learning progress of pair of words
        """
        cursor = self.__connection.cursor()
        cursor.execute('''
            UPDATE Practices
            SET practicing_points_left = ?
            WHERE id = ?
            ''', [practice.points_left, practice.id]
            )
        self.__connection.commit()


    def create_practiced_pair(self, person_id, practice: Practice):
        """Creates new pair of practised words in database.

        Contains user id, pair of word id, learning progress points.

        Args:
            person_id (int):        rowid for user from database table Persons
            practice (Practice):    object Practice containing new pair of practised words
        """
        cursor = self.__connection.cursor()
        cursor.execute('''
            INSERT INTO Practices (
                person_id, translation_id, practicing_points_left
                )
            VALUES (?,?,?)
            ''', [person_id, practice.translation_id, practice.points_left]
            )
        self.__connection.commit()


    def delete_all(self):
        """Deletes all rows from table Practices."""
        cursor = self.__connection.cursor()

        cursor.execute('DELETE FROM Practices')

        self.__connection.commit()


practise_repository = PractiseRepository(get_database_connection())
