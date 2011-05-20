from wordChooser import WordChooser
from wordValidator import WordValidator

class WordGuessGame:
    """ An instance of a game of GuessWord """
    def __init__(self, screen):
        """ Initialize game """
        self.screen = screen
        self.score = 0
        self.exit = False
        
        self.SCORES = [1000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]
        
    def start(self):
        """ Starts the game, runs until told to exit """
        while not self.exit:
            if not WordValidator.nextWord():
                break
            self.gameLoop()
            
        self.screen.winGame()
            
    def gameLoop(self):
        """ Run a single iteration of the game aka solve for one word """
        for numGuesses in range(11):
            if self.runGuess(numGuesses):
                return
        
        self.screen.gameOver(self.score)      # If you get here Game Over
        self.exit = True
        
    def runGuess(self, numGuesses):
        """ Gets and evaluates one guess and increases the score """
        guess = self.screen.guess(numGuesses)                      # Get initial guess
        if WordValidator.correctWord(guess):
            self.score = self.score + self.SCORES[numGuesses]
            self.screen.winRound(guess, self.score)
            return True
            
        response = WordValidator.validate(guess)                   # Validate the guess
        self.screen.respond(response)                                    # Has Screen display the response to the guess
        
        