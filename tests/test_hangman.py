import unittest
from unittest.mock import patch, call, Mock

from hangman import Hangman


class TestHangman(unittest.TestCase):

    def test_word_win(self):

        self.assertEqual(True, Hangman.check_word_win(self, 'packers', 'packers'))
        self.assertEqual(True, Hangman.check_word_win(self, 'vikings', 'vikings'))

    def test_word_lose(self):

        self.assertEqual(False, Hangman.check_word_lose(self, 'packers', 'vikings'))
        self.assertEqual(False, Hangman.check_word_lose(self, 'vikings', 'packers'))


    @patch('builtins.input', side_effect=['ww', '10', 'a', 's'])
    def test_invalid_letters_guessed(self, mock_input):

        game = Hangman()
        guess = game.letters_guessed('abc')
        self.assertEqual(guess, 's')


    @patch('builtins.input', side_effect=['s'])
    def test_letters_guessed(self, mock_input):

        game = Hangman()
        guess = game.letters_guessed('abc')
        self.assertEqual(guess, 's')


if __name__ == '__main__':
    unittest.main()
