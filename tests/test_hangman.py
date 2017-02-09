import unittest
from unittest.mock import patch, call, Mock

from hangman import Hangman


class TestHangman(unittest.TestCase):

    def test_word_win(self):

        self.assertEqual(True, Hangman.check_word_win(self, 'packers', 'packers'))
        self.assertEqual(True, Hangman.check_word_win(self, 'vikings', 'vikings'))

    def test_word_lose(self):

        self.assertEquals(False, Hangman.check_word_lose(self, 'packers', 'vikings'))
        self.assertEquals(False, Hangman.check_word_lose(self, 'vikings', 'packers'))


    @patch('builtins.input', side_effect=['ww', '10', 'a', 's'])
    def test_invalid_letters_guessed(self, mock_input):

        # Test invalid guesses
        game = Hangman()
        guess = game.letters_guessed('abc')
        self.assertEqual(guess, 's')


    @patch('builtins.input', side_effect=['s'])
    def test_letters_guessed(self, mock_input):

        game = Hangman()
        guess = game.letters_guessed('abc')
        self.assertEqual(guess, 's')


        #self.assertNotIn(Hangman.letters_guessed(self, 'abc'), mock_input)

    '''TODO: get this working
    def test_show_game_board(self):'''

    @patch('hangman.Hangman.play_one_game', return_value='no')
    def test_play_one_game(self, mock_input):
        self.assertTrue(Hangman.play_one_game(self), mock_input)


if __name__ == '__main__':
    unittest.main()
