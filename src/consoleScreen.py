from wordGuessGame import WordGuessGame
from wordValidator import WordValidator

class ConsoleScreen:
    """ Allows use of Command-Line console as the Screen """
    def __init__(self):
        """ Initialize ConsoleScreen """
        self.options = [self.startGame, self.instructions, self.exit]
    
    def mainMenu(self):
        """ Prints the Main Menu options and listens for response """
        response = 0
        while response is not 3:
            print "Choose an option:"
            print "1. Start Game"
            print "2. Instructions"
            print "3. Exit"
            
            response = int(raw_input())
            if response not in range(1, 4):
                print "\nSorry, please pick a # between 1 and 3\n"
            else:
                self.options[response-1]()
            
    def startGame(self):
        """ Starts a Game of GuessWord """
        game = WordGuessGame(self)
        game.start()
        
    def guess(self,):
        """ Prompts for a guess, and then reads a guess """
        while True:
            print "Enter your guess!"
            guess = raw_input()
            response = WordValidator.invalidGuess(guess)
            if not response:
                return guess
            print response
            
    
    def printScore(self, score):
        """ Prints the given Score """
        print "\nYou scored:", score, "points\n"
        
    def instructions(self):
        """ Prints the instructions to the console """
        print """10 attempts to solve word, after initial guess
                 More points for less tries
                 Feedback:
                    U: Letter is higher in the alphabet
                    D: Letter is lower
                    R: Letter is within 5 of the guess to the right
                    L: Ditto but left
                    C: Letter is within 5 of guess in this spot
                    X: Wrong!!! -- Allows computer to be a jerk on occasion 
                    Correct Letters appear as lower-case version of guess"""
        
    def exit(self):
        """ Exits the game """
        print "Thanks for playing!"
            
            