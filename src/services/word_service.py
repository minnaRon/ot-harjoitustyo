from entities.word import Word

from repositories.word_repository import (
    word_repository as default_word_repository
)


class WordAddingError(Exception):
    pass


class WordService:

    def __init__(self, word_repository=default_word_repository):
        self.__word_repository = word_repository
        self.__languages = {'suomi': 'Finnish', 'englanti': 'English'}

    def _add_words(self, words_orig, lang_orig, words_transl, lang_transl):
        for i in range(len(words_orig)):
            self.add_word_with_translation(
                words_orig[i], self.__languages[lang_orig], words_transl[i], self.__languages[lang_transl])

    def add_word_with_translation(self, word_orig, lang_orig, word_transl, lang_transl):
        try:
            self.__word_repository.add_pair_word_and_translation(
                word_orig, lang_orig, word_transl, lang_transl
            )
        except:
            raise WordAddingError(
                f'Sanojen lisäys ei onnistunut, tarkista antamasi tiedot ja yritä uudelleen'
            )


word_service = WordService()
