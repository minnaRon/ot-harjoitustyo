import unittest
from repositories.word_repository import word_repository
from entities.word import Word

class TestWordRepository(unittest.TestCase):
    def setUp(self):
        word_repository.delete_all()
        word_repository.add_pair_word_and_translation(Word('sana0', 'Finnish'), Word('word0', 'English'))

    def test_method_get_word_id_returns_id(self):
        word = Word('sana0', 'Finnish')
        self.assertEqual(word_repository._get_word_id(word),1)
