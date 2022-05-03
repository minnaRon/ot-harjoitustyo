from database_connection import get_database_connection


class WordRepository:
    """Class takes care of database operations concerning word operations."""
    def __init__(self, connection):
        """Constructor creates database connection

        Args:
            connection (object):    object of database connection
        """
        self.__connection = connection


    def _add_word_returning_id(self, word, lang):
        """Creates new word in database and returns rowid of the word.

        Args:
            word (string): word
            lang (string): language of word

        Returns:
            int: rowid of the word
        """
        cursor = self.__connection.cursor()

        sql = '''INSERT INTO Words (word, language)
            VALUES (:word, :lang)
            '''
        dictionary = {'word': word, 'lang': lang}
        cursor.execute(sql, dictionary)

        self.__connection.commit()

        return cursor.lastrowid


    def add_pair_word_and_translation(self, word_orig, lang_orig, word_transl, lang_transl) -> int:
        """Adds pair of words in the database and returns rowid of the pair.

        Args:
            words_orig (string):    original word
            lang_orig (string):     language of the original word
            words_transl (string):  translation of word
            lang_transl (string):   language of the translation

        Returns:
            int: rowid of the pair of words
        """
        word_orig_id = self._get_word_id(word_orig, lang_orig)
        if not word_orig_id:
            word_orig_id = self._add_word_returning_id(word_orig, lang_orig)

        word_transl_id = self._get_word_id(word_transl, lang_transl)
        if not word_transl_id:
            word_transl_id = self._add_word_returning_id(
                word_transl, lang_transl)

        word_pair_id = self._get_word_pair(word_orig_id, word_transl_id)

        if not word_pair_id:
            cursor = self.__connection.cursor()

            sql = '''INSERT INTO Translations (word_orig_id, word_transl_id)
                    VALUES (:word_orig_id, :word_transl_id)
                    '''
            dictionary = {'word_orig_id': word_orig_id,
                          'word_transl_id': word_transl_id}

            cursor.execute(sql, dictionary)

            self.__connection.commit()

            word_pair_id = cursor.lastrowid

        return word_pair_id


    def _get_word_pair(self, word_orig_id, word_transl_id):
        """Returns id of the pair of words if exists.

        Args:
            word_orig_id (int):   id of the original word
            word_transl_id (int): id of the translation of the original word

        Returns:
            int: id of the pair of words
        """
        cursor = self.__connection.cursor()

        cursor.execute('''
            SELECT id FROM Translations
            WHERE (word_orig_id=:word_orig_id AND word_transl_id=:word_transl_id)
            OR (word_orig_id=:word_transl_id AND word_transl_id=:word_orig_id)
        ''', {'word_orig_id': word_orig_id, 'word_transl_id': word_transl_id}
        )
        result = cursor.fetchone()
        return result[0] if result else result


    def add_all_words_from_file_to_database(self, file):
        """Transfers all words from csv -file to database.

        If used separator ';' and pair of words are placed below each other.

        Args:
            file (csv):     contains pair of words separated with character ';'
        """
        with open(file, encoding='utf-8') as file_words:
            for row in file_words:
                parts = row.strip().split(";")
                word_orig, word_transl = parts
                self.add_pair_word_and_translation(
                    word_orig, "English", word_transl, "Finnish")


    def _get_word_id(self, word, lang):
        """Returns id of the word

        Args:
            word (string): word
            lang (string): language of the word

        Returns:
            int: id of the word
        """
        cursor = self.__connection.cursor()

        cursor.execute('''
            SELECT id FROM Words
            WHERE word=? AND language=?
        ''', [word, lang]
        )
        result = cursor.fetchone()
        return result[0] if result else result


word_repository = WordRepository(get_database_connection())
