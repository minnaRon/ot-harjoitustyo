from database_connection import get_database_connection
from entities.practise import Practice


class PractiseRepository:

    def __init__(self, connection):
        self.__connection = connection


    def get_words_with_translations(self, lang_orig, lang_transl):
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
        cursor = self.__connection.cursor()
        cursor.execute('''
            UPDATE Practices
            SET practicing_points_left = ?
            WHERE id = ?
            ''', [practice.points_left, practice.id]
            )
        self.__connection.commit()


    def create_practiced_pair(self, person_id, practice: Practice):
        cursor = self.__connection.cursor()
        cursor.execute('''
            INSERT INTO Practices (
                person_id, translation_id, practicing_points_left
                )
            VALUES (?,?,?)
            ''', [person_id, practice.translation_id, practice.points_left]
            )
        self.__connection.commit()


practise_repository = PractiseRepository(get_database_connection())
