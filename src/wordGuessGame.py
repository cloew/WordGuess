from wordChooser import WordChooser

class WordGuessGame:
    """ An instance of a game of GuessWord """
    def __init__(self, screen):
        """ Initialize game """
        self.screen = screen
        self.wordLength = 3
        self.score = 0
        self.exit = 0
        
    def start(self):
        """ Starts the game, runs until told to exit """
        while not self.exit:
            self.word = WordChooser.pickWord(self.wordLength)
            self.gameLoop()
            self.wordLength = self.wordLength+1
            if self.wordLength > WordChooser.MAXWORDLENGTH:
                self.exit = 1
                
        self.screen.printScore(self.score)
            
    def gameLoop(self):
        """ Run a single iteration of the game aka solve for one word """