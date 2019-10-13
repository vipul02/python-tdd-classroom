
import unittest
from src.string_exercise import StringExercise


class TestExercise(unittest.TestCase):

    def setUp(self):
        self.string_exercise = StringExercise()   # Instantiate object of StringExercise class for testing

    def test_reverse_string(self):
        text = "foobar"
        expected = "raboof"
        actual = self.string_exercise.reverse_string(text)
        self.assertEqual(expected, actual)

    def test_is_english_vowel_when_vowel(self):
        self.assertTrue(self.string_exercise.is_english_vowel('a'))
        self.assertTrue(self.string_exercise.is_english_vowel('e'))
        self.assertTrue(self.string_exercise.is_english_vowel('i'))
        self.assertTrue(self.string_exercise.is_english_vowel('o'))
        self.assertTrue(self.string_exercise.is_english_vowel('u'))
        self.assertTrue(self.string_exercise.is_english_vowel('A'))
        self.assertTrue(self.string_exercise.is_english_vowel('E'))
        self.assertTrue(self.string_exercise.is_english_vowel('I'))
        self.assertTrue(self.string_exercise.is_english_vowel('O'))
        self.assertTrue(self.string_exercise.is_english_vowel('U'))

    def test_is_english_vowel_when_not_vowel(self):
        self.assertFalse(self.string_exercise.is_english_vowel('b'))
        self.assertFalse(self.string_exercise.is_english_vowel('?'))
        self.assertFalse(self.string_exercise.is_english_vowel('Z'))

    def test_find_longest_word(self):
        text = "Three tomatoes are walking down the street"
        expected = "tomatoes"
        actual = self.string_exercise.find_longest_word(text)
        self.assertEqual(expected, actual)

        text = "foo foo1 foo2 foo3"
        expected = "foo1"
        actual = self.string_exercise.find_longest_word(text)
        self.assertEqual(expected, actual)

    def test_get_word_lengths(self):
        text = "Three tomatoes are walking down the street"
        expected = [5, 8, 3, 7, 4, 3, 6]
        actual = self.string_exercise.get_word_lengths(text)
        self.assertEqual(expected, actual) 

    def tearDown(self):
        pass   # If needed, do final unstubbing/unmocking here, like calling unittest.unstub()
