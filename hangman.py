from words import Word
import emoji

class Hangman:

    def __init__(self):
        random_word = Word().get_random_word()
        self.random_word = random_word[:-1]
        self.hangman_board_image = ['''

          +-------+
          |       |
                  |
                  |
                  |
                  |
    ----------------''', '''

          +-------+
          |       |
         :frowning:        |
                  |
                  |
                  |
    ----------------''', '''

          +-------+
          |       |
         :grimacing:        |
          0       |
                  |
                  |
    ----------------''', '''

          +-------+
          |       |
         :sweat:        |
         /0       |
                  |
                  |
    ----------------''', '''

          +-------+
          |       |
         :fearful:        |
         /0\      |
                  |
                  |
    ----------------''', '''

          +-------+
          |       |
         :cry:        |
         /0\      |
         /        |
                  |
    ----------------''', '''

          +-------+
          |       |
         :dizzy_face:        |
         /0\      |
         / \      |
                  |
    ----------------''']

    def letters_guessed(self, guessed):

        while True:
            guess = input("Guess a letter!").lower()
            # checking to make sure there is only 1 letter entered
            if len(guess) != 1:
                print("Please enter only 1 letter!")
            # checking to make sure a letter was entered
            elif guess not in "abcdefghijklmnopqrstuvwxyz49":
                print("Please enter a letter, NOT a number! *Except 4 or 9*")
            # checking to see if it has already been entered
            elif guess in guessed:
                print("You have already guessed that letter! Try again.")
            else:
                return guess

    def play_again(self):
        # gives the user the option to play again or not
        return input("Do you want to play again? (yes or no)").lower().startswith("y")


    def show_game_board(self, hangman_board_image, incorrect_guess, correct_guess, picked_word):
        # printing the game board
        print(emoji.emojize(hangman_board_image[len(incorrect_guess)], use_aliases=True))
        print()
        # printing the missed letters
        print("Incorrect letters:", end=" ")
        for letter in incorrect_guess:
            print(letter, end=" ")
        print()

        hidden_letters = " "
        # replacing the hidden letters with the correctly guessed letters
        for i in range(len(picked_word)):
            if picked_word[i] in correct_guess:
                hidden_letters += picked_word[i]
            else:
                hidden_letters += "_"
        # displaying the hidden word with spaces in between them
        for letter in hidden_letters:
            print(letter, end=" ")
        print()

    # check to see if the player has won
    def check_word_win(self, correct_letters, picked_word):
        all_correct_letters = True
        for i in range(len(picked_word)):
            # checking to see if a letter is not in the picked hidden word
            if picked_word[i] not in correct_letters:
                all_correct_letters = False
                break
        return all_correct_letters

    # check to see if the player has guessed 6 times and lost
    def check_word_lose(self, missed_letters):
        if len(missed_letters) == len(self.hangman_board_image) - 1:
            return True
        return False

    def initialize_game(self):
        print("Welcome to NFL hangman! \n\n1 of 32 NFL team names will be randomly selected as the word. \n"
              "You have 6 wrong guesses to try and guess the team name. Numbers are not allowed except 4 and 9!")
        self.incorrect_letters = ""
        self.correct_letters = ""
        self.user_win = False
        self.user_lose = False
        self.picked_word = self.random_word

    def user_wants_to_play(self):

        while True:
            self.show_game_board(self.hangman_board_image, self.incorrect_letters, self.correct_letters, self.picked_word)

            # getting the user input letter
            guess = self.letters_guessed(self.incorrect_letters + self.correct_letters)
            # if the letter is in the picked word it will be added to the string and checked to see if the user won
            if guess in self.picked_word:
                self.correct_letters = self.correct_letters + guess
                self.user_win = self.check_word_win(self.correct_letters, self.picked_word)
            # if the letter is not in the picked word it will be added to the incorrect letter string and checked to see if the
            # user has lost
            else:
                self.incorrect_letters = self.incorrect_letters + guess
                self.user_lose = self.check_word_lose(self.incorrect_letters)
            # if the user wins or user loses is true it will show the user if they won or lost
            if self.user_win or self.user_lose:
                self.show_game_board(self.hangman_board_image, self.incorrect_letters, self.correct_letters, self.picked_word)
                print()
                if self.user_win:
                    print("Congratulations! The random team name picked was", self.picked_word + ".", "You win!")
                    break
                else:
                    print("Sorry, you have run out of guesses :(\nAfter 6 missed guesses the word was", self.picked_word)
                    break

    def play_one_game(self):
        # asking the user if they want to play the game again
        if self.play_again():
            # if the user wants to play again, it will reset everything and start over
            self.random_word = Word().get_random_word()
            self.random_word = self.random_word[:-1]
            Hangman.game_run(self)

        # if the user doesn't want to play anymore the game will end
        else:
            print()
            print("Thank you for playing NFL Hangman!")



    def game_run(self):

        self.initialize_game()

        self.user_wants_to_play()

        self.play_one_game()







