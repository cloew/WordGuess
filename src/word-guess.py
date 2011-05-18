from consoleScreen import ConsoleScreen

import random

if __name__ == "__main__":
    """ Main enrty point for Word Guess Game """
    random.seed()
    screen = ConsoleScreen()
    screen.mainMenu()