from wordChooser import WordChooser
from wordValidator import WordValidator

class WordGuessGame:
    """ An instance of a game of GuessWord """
    def __init__(self, screen):
        """ Initialize game """
        self.screen = screen
        self.score = 0
        self.exit = 0
        
    def start(self):
        """ Starts the game, runs until told to exit """
        while not self.exit:
            if not WordValidator.nextWord():
                break
            self.gameLoop()
      
        self.screen.printScore(self.score)
            
    def gameLoop(self):
        """ Run a single iteration of the game aka solve for one word """
        self.screen.guess()
        