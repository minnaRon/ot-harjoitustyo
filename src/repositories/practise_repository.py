from database_connection import get_database_connection


class PractiseRepository:

    def __init__(self, connection):
        self.__connection = connection

    def get_words_with_translations(self, lang_orig, lang_transl):
        cursor = self.__connection.cursor()
        cursor.execute('''
                SELECT O.word, T.word
                FROM Words O 
                JOIN Translations TR ON TR.word_orig_id = O.id
                JOIN Words T ON T.id = TR.word_transl_id
                WHERE O.language = ?
                AND T.language = ?
                ORDER BY length(O.word)
                ''', [lang_orig, lang_transl]
        )
        rows = cursor.fetchall()

        return [(row[0], row[1]) for row in rows]


practise_repository = PractiseRepository(get_database_connection())
