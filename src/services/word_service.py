from repositories.word_repository import (
    word_repository as default_word_repository
)
from entities.word import Word


class WordAddingError(Exception):
    pass


class WordService:
    """Class takes care of word operations."""

    def __init__(self, word_repository=default_word_repository):
        """Constructor

        Args:
            word_repository (class):    Defaults to default_word_repository.

        Other object variables:
            self._languages (dict):     Contains translations of language names fin->eng

        """
        self._word_repository = word_repository
        self._languages = {'suomi': 'Finnish', 'englanti': 'English'}


    def _add_words(self, words_orig, lang_orig, words_transl, lang_transl):
        """Handles user input regarding list of words and translations.

        Calls method add_word_with_translation to handle word pairs separately.

        Args:
            words_orig (list):      original words as a list
            lang_orig (string):     language of the original word
            words_transl (list):    translation of words as a list
            lang_transl (string):   language of the translation
        """
        if lang_orig == 'suomi':
            words_orig, words_transl = words_transl, words_orig
            lang_orig, lang_transl = lang_transl, lang_orig

        for i, word_orig in enumerate(words_orig, start=0):
            self.add_word_with_translation(
                Word(word_orig, self._languages[lang_orig]),
                Word(words_transl[i], self._languages[lang_transl])
            )


    def add_word_with_translation(self, word_orig, word_transl):
        """Calls word_repository to add a word and a translation to the database.

        Args:
            words_orig (string):    original word
            lang_orig (string):     language of the original word
            words_transl (string):  translation of word
            lang_transl (string):   language of the translation

        Raises:
            WordAddingError:    message if adding words to the database failed.
        """
        try:
            self._word_repository.add_pair_word_and_translation(
                word_orig, word_transl
            )
        except:
            raise WordAddingError(
                'Sanojen lisäys ei onnistunut, tarkista antamasi tiedot ja yritä uudelleen'
            )


word_service = WordService()
