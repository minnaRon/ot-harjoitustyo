from database_connection import get_database_connection
from entities.practise import PracticedWordPair


class PractiseRepository:
    """Class takes care of database operations related to practiced pairs of words."""
    def __init__(self, connection):
        """Constructor creates database connection

        Args:
            connection (object):    object of database connection
        """
        self.__connection = connection


    def get_words_with_translations(self, lang_orig, lang_transl):
        """Returns PracticedWordPair objects of all pairs of words where languages are as asked.

        Args:
            lang_orig (string):     language of origin word
            lang_transl (string):   language of translation

        Returns:
            object PracticedWordPair:  object contains origin word, translation, id of word pair
        """
        cursor = self.__connection.cursor()
        cursor.execute('''
                SELECT O.word, T.word, WP.id
                FROM Words O
                JOIN Word_pairs WP ON WP.word_orig_id = O.id
                JOIN Words T ON T.id = WP.word_transl_id
                WHERE O.language = ?
                AND T.language = ?
                ORDER BY length(O.word)
                ''', [lang_orig, lang_transl]
        )
        rows = cursor.fetchall()

        return [PracticedWordPair(row[0], row[1], row[2]) for row in rows]


    def get_practices(self, person_id):
        """Returns PracticedWordPair objects where person id is as asked.

        Args:
            person_id (int):    user id

        Returns:
            dict of objects PracticedWordPair:  dictionary contains objects of PracticedWordPair
                                                object contains:
                                                object id, pair of words id, practicing points left
        """
        cursor = self.__connection.cursor()
        cursor.execute('''
                SELECT id, word_pair_id, practicing_points_left
                FROM Practice_progress
                WHERE person_id = ?
                ''', [person_id]
        )
        rows = cursor.fetchall()

        return {row[1]:PracticedWordPair("", "", row[1], row[0], person_id, row[2]) for row in rows}


    def save_points(self, practiced_word_pair: PracticedWordPair):
        """Saves learning progress points of user concerning pair of words.

        Args:
            practiced_word_pair (PracticedWordPair):    object contains learning progress
                                                        of pair of words
        """
        cursor = self.__connection.cursor()
        cursor.execute('''
            UPDATE Practice_progress
            SET practicing_points_left = ?
            WHERE id = ?
            ''', [practiced_word_pair.points_left, practiced_word_pair.id]
            )
        self.__connection.commit()


    def create_practiced_pair(self, person_id, practiced_word_pair: PracticedWordPair):
        """Creates new pair of practised words in database.

        Contains user id, pair of word id, learning progress points.

        Args:
            person_id (int):        rowid for user from database table Persons
            practiced_word_pair (PracticedWordPair):    object PracticedWordPair
                                                        containing new pair of practised words
        """
        cursor = self.__connection.cursor()
        cursor.execute('''
            INSERT INTO Practice_progress (
                person_id, word_pair_id, practicing_points_left
                )
            VALUES (?,?,?)
            ''', [person_id, practiced_word_pair.translation_id, practiced_word_pair.points_left]
            )
        self.__connection.commit()


    def delete_all(self):
        """Deletes all rows from table Practices."""
        cursor = self.__connection.cursor()

        cursor.execute('DELETE FROM Practice_progress')

        self.__connection.commit()


practise_repository = PractiseRepository(get_database_connection())
