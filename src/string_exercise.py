class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        if character.upper() in ['A', 'E', 'I', 'O', 'U']:
            return True
        else:
            return False 

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        
        words = sentence.split(' ')
        words_length = self.get_word_lengths(sentence)
        return words[words_length.index(max(words_length))]

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        return list(map(lambda x: len(x), text.split(' ')))