
import unittest
from src.exercises import reverse_list, reverse_string, is_english_vowel, find_longest_word, get_word_lengths


class TestExercise(unittest.TestCase):

    def setUp(self):
        pass  # Do initial common setup here, if needed

    def test_reverse_list(self):
        expected = [5, 4, 3, 2, 1]
        actual = reverse_list([1, 2, 3, 4, 5])
        self.assertEqual(expected, actual)

        expected = [6, 5, 4, 3, 2, 1]
        actual = reverse_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(expected, actual)    

    def test_reverse_string(self):
        text = "foobar"
        expected = "raboof"
        actual = reverse_string(text)
        self.assertEqual(expected, actual)

    def test_is_english_vowel_when_vowel(self):
        self.assertTrue(is_english_vowel('a'))
        self.assertTrue(is_english_vowel('e'))
        self.assertTrue(is_english_vowel('i'))
        self.assertTrue(is_english_vowel('o'))
        self.assertTrue(is_english_vowel('u'))
        self.assertTrue(is_english_vowel('A'))
        self.assertTrue(is_english_vowel('E'))
        self.assertTrue(is_english_vowel('I'))
        self.assertTrue(is_english_vowel('O'))
        self.assertTrue(is_english_vowel('U'))

    def test_is_english_vowel_when_not_vowel(self):
        self.assertFalse(is_english_vowel('b'))
        self.assertFalse(is_english_vowel('?'))
        self.assertFalse(is_english_vowel('Z'))

    def test_find_longest_word(self):
        text = "Three tomatoes are walking down the street"
        expected = "tomatoes"
        actual = find_longest_word(text)
        self.assertEqual(expected, actual)

        text = "foo foo1 foo2 foo3"
        expected = "foo1"
        actual = find_longest_word(text)
        self.assertEqual(expected, actual)

    def test_get_word_lengths(self):
        text = "Three tomatoes are walking down the street"
        expected = [5, 8, 3, 7, 4, 3, 6]
        actual = get_word_lengths(text)
        self.assertEqual(expected, actual) 

    def tearDown(self):
        pass   # If needed, do final unstubbing/unmocking here, like calling unittest.unstub()
