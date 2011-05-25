from consoleScreen import ConsoleScreen
from wordChooser import WordChooser

import random
import sys

if __name__ == "__main__":
    """ Main enrty point for Word Guess Game """
    WordChooser.loadWords(sys.argv[0].split("word-guess.py")[0])
    random.seed()
    screen = ConsoleScreen()
    screen.mainMenu()