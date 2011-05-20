from wordChooser import WordChooser
from wordValidator import WordValidator

class WordGuessGame:
    """ An instance of a game of GuessWord """
    def __init__(self, screen):
        """ Initialize game """
        self.screen = screen
        self.score = 0
        self.exit = 0
        
        self.SCORES = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]
        
    def start(self):
        """ Starts the game, runs until told to exit """
        while not self.exit:
            if not WordValidator.nextWord():
                break
            self.gameLoop()
      
        self.screen.score(self.score)
            
    def gameLoop(self):
        """ Run a single iteration of the game aka solve for one word """
        self.runGuess(0)
        for numGuesses in range(10):
            self.runGuess(numGuesses)
        
    def runGuess(self, numGuesses):
        """ Gets and evaluates one guess and increases the score """
        guess = self.screen.guess()                      # Get initial guess
        response = WordValidator.validate(guess) # Validate the guess
        self.score = self.score + self.SCORES[numGuesses]
        self.screen.respond(response)                  # Has Screen display the response to the guess
        
        