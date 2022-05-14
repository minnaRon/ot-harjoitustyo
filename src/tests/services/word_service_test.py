import unittest
from unittest.mock import Mock
from services.word_service import WordService
from entities.word import Word

class TestWordService(unittest.TestCase):
    def setUp(self):
        self.word_repo_mock = Mock()
        self.word_service = WordService(self.word_repo_mock)

    def test_has_languages_in_class_attribute(self):
        self.assertIsNotNone(self.word_service._languages)

    def test_when_class_inside_call_add_word_pair_with_translation_then_method_calls_repository_to_add_pair(self):
        word1 = Word('sana', 'Finnish')
        word2 = Word('word', 'English')
        self.word_service.add_word_with_translation(word1, word2)
        self.word_repo_mock.add_pair_word_and_translation.assert_called_once_with(word1, word2)

    def test_when_word_view_calls_add_words_then_method_calls_repository_to_add_pair(self):
        self.word_service._add_words(['sana', 'toinen'], 'suomi', ['word', 'another'], 'englanti')
        self.word_repo_mock.add_pair_word_and_translation.assert_called()
