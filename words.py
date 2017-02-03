import random
import sys


class Word:

    #  initializing the word list
    def __init__(self):
        self.word_list = []

    #  a function to get a random word from the word list
    def get_random_word(self):
        self.read_file()
        # picking a random word from the list
        word = random.randint(0, len(self.word_list) - 1)
        return self.word_list[word]

    # a function to read the txt file
    def read_file(self):

        try:
            # opening the txt file
            file = open("nfl_team_names.txt", 'rt')

        except IOError:
            print("Could not open file:", file)
            sys.exit()

        # reading each line in the txt file
        while True:
            file_read = file.readline()
            if file_read == '':
                break

            else:
                self.word_list.append(file_read)  # adding each line to the list

        file.close()

        return self.word_list