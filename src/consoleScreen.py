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
            
            temp = raw_input()
            if not temp.isdigit() or int(temp) not in range(1, 4):
                print "\nSorry, please pick a # between 1 and 3\n"
            else:
                response = int(temp)
                self.options[response-1]()
            
    def startGame(self):
        """ Starts a Game of GuessWord """
        game = WordGuessGame(self)
        game.start()
        
    def guess(self, numGuesses, potScore):
        """ Prompts for a guess, and then reads a guess """
        while True:
            print "Enter your", len(WordValidator.target), "letter guess!"
            print "Guess correctly to score %d points!" % potScore
            guess = raw_input()
            response = WordValidator.invalidGuess(guess)
            if not response:
                return guess.lower()
            print response
            
    def respond(self, response):
        """ Responds to the previous guess by printing the response string """
        print response
            
    
    def score(self, score):
        """ Prints the given Score """
        print "\nYou scored:", score, "points\n"
        
    def winRound(self, guess, score):
        """ Prints that the user won the round """
        print "Congratulations '%s' was the word!" % guess
        self.score(score)
        
    def winGame(self):
        """ Prints that the user won the game """
        print "YOU WON THE GAME!"
        
    def gameOver(self, score):
        """ Prints that the game is over """
        print "GAME  OVER"
        print "You ran out of guesses"
        print "The correct answer was", WordValidator.target
        self.score(score)
        
    def instructions(self):
        """ Prints the instructions to the console """
        print """10 attempts to solve word, after initial guess
                 More points for less tries
                 Feedback:
                    U: Letter is higher in the alphabet (closer to 'A')
                    D: Letter is lower (closer to 'Z')
                    R: Letter is within 5 of the guess to the right
                    L: Ditto but left
                    C: Letter is within 5 of guess in this spot
                    X: Wrong!!! -- Allows computer to be a jerk on occasion 
                    Any lower-case letter is the correct letter in the correct spot """
        
    def exit(self):
        """ Exits the game """
        print "Thanks for playing!"
            
            