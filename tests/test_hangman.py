import unittest
from unittest.mock import patch

from hangman import Hangman


class TestHangman(unittest.TestCase):

    def test_word_win(self):
        # testing to check to see if the winning word is equal to the word the user entered
        self.assertEqual(True, Hangman.check_word_win(self, 'packers', 'packers'))
        self.assertEqual(True, Hangman.check_word_win(self, 'vikings', 'vikings'))

    def test_word_lose(self):
        # testing to check to see if the winning word is not equal to the word the user entered
        self.assertEqual(False, Hangman.check_word_lose(self, 'packers', 'vikings'))
        self.assertEqual(False, Hangman.check_word_lose(self, 'vikings', 'packers'))


    @patch('builtins.input', side_effect=['ww', '10', 'a', 's'])
    def test_invalid_letters_guessed(self, mock_input):
        # testing each part to make sure the user can't enter two letters, a non valid number, or the same latter twice
        game = Hangman()
        guess = game.letters_guessed('abc')
        self.assertEqual(guess, 's')


    @patch('builtins.input', side_effect=['s'])
    def test_letters_guessed(self, mock_input):
        # testing to see if the user guess will pass
        game = Hangman()
        guess = game.letters_guessed('abc')
        self.assertEqual(guess, 's')

    def test_show_game_board(self):
        # testing the game board
        game = Hangman()
        packer = game.show_game_board('c', 'packers')
        viking = game.show_game_board('i', 'vikings')
        # showing where the letters are placed in the word
        self.assertTrue('c', packer)
        self.assertTrue('i', viking)
        # showing that the letter is not in the word
        self.assertFalse(Hangman.show_game_board(self, 'w', 'vikings'))
        self.assertFalse(Hangman.show_game_board(self, 'w', 'packers'))

    @patch('builtins.input', side_effect=['no'])
    def test_play_one_game_no(self, mock_input):
        # testing if the user doesn't want to play another game
        game = Hangman()
        guess = game.play_one_game()
        self.assertTrue('no', guess)

if __name__ == '__main__':
    unittest.main()
