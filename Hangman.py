from Words import Word
import emoji

class HangMan:

    def __init__(self):
        randomWord = Word().get_random_word()
        self.randomWord = randomWord[:-1]
        self.hangmanBoardImage = ['''

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
          |       |
                  |
                  |
    ----------------''', '''

          +-------+
          |       |
         :sweat:        |
         /|       |
                  |
                  |
    ----------------''', '''

          +-------+
          |       |
         :fearful:        |
         /|\      |
                  |
                  |
    ----------------''', '''

          +-------+
          |       |
         :cry:        |
         /|\      |
         /        |
                  |
    ----------------''', '''

          +-------+
          |       |
         :dizzy_face:        |
         /|\      |
         / \      |
                  |
    ----------------''']

    def letters_guessed(self, guessed):

        while True:
            # asking the user to guess a letter
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


    def show_game_board(self, hangmanBoardImage, incorrectGuess, correctGuess, pickedWord):
        # printing the game board
        print(emoji.emojize(hangmanBoardImage[len(incorrectGuess)], use_aliases=True))
        print()
        # printing the missed letters
        print("Incorrect letters:", end=" ")
        for letter in incorrectGuess:
            print(letter, end=" ")
        print()

        hiddenLetters = " "
        # replacing the hidden letters with the correctly guessed letters
        for i in range(len(pickedWord)):
            if pickedWord[i] in correctGuess:
                hiddenLetters += pickedWord[i]
            else:
                hiddenLetters += "_"
        # displaying the hidden word with spaces in between them
        for letter in hiddenLetters:
            print(letter, end=" ")
        print()

    # check to see if the player has won
    def check_word_win(self, correctLetters, pickedWord):
        allCorrectLetters = True
        for i in range(len(pickedWord)):
            # checking to see if a letter is not in the picked hidden word
            if pickedWord[i] not in correctLetters:
                allCorrectLetters = False
                break
        return allCorrectLetters

    # check to see if the player has guessed 6 times and lost
    def check_word_lose(self, missedLetters):
        if len(missedLetters) == len(self.hangmanBoardImage) - 1:
            return True
        return False

    def game_run(self):
        print("Welcome to NFL hangman! \n\n1 of 32 NFL team names will be randomly selected as the word. \n"
              "You have 6 wrong guesses to try and guess the team name. Numbers are not allowed except 4 and 9!")
        incorrectLetters = ""
        correctLetters = ""
        userWin = False
        userLose = False
        pickedWord = self.randomWord

        while True:
            self.show_game_board(self.hangmanBoardImage, incorrectLetters, correctLetters, pickedWord)

            # getting the user input letter
            guess = self.letters_guessed(incorrectLetters + correctLetters)
            # if the letter is in the picked word it will be added to the string and checked to see if the user won
            if guess in pickedWord:
                correctLetters = correctLetters + guess
                userWin = self.check_word_win(correctLetters, pickedWord)
            # if the letter is not in the picked word it will be added to the incorrect letter string and checked to see if the
            # user has lost
            else:
                incorrectLetters = incorrectLetters + guess
                userLose = self.check_word_lose(incorrectLetters)
            # if the user win or user lose is true it will show the user if they won or lost
            if userWin or userLose:
                self.show_game_board(self.hangmanBoardImage, incorrectLetters, correctLetters, pickedWord)
                print()
                if userWin:
                    print("Congratulations! The random team name picked was", pickedWord + ".", "You win!")
                else:
                    print("Sorry, you have run out of guesses :(\nAfter 6 missed guesses the word was", pickedWord)

                # asking the user if they want to play the game again
                if self.play_again():
                    # if the user wants to play again, it will reset everything and start over
                    self.randomWord = Word().get_random_word()
                    self.randomWord = self.randomWord[:-1]
                    HangMan.game_run(self)

                # if the user doesn't want to play anymore the game will end
                else:
                    print()
                    print("Thank you for playing NFL Hangman!")
                    break




