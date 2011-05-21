from wordChooser import WordChooser
import random

class WordValidator:
    """ Validates a guess related to the answer """
    
    INVALID_LENGTH = "Must be " + str(WordChooser.FIRSTLENGTH) + " characters long."
    INVALID_CHARACTERS = "Guess can only conatin alphabet characters"
    target = None
    
    @staticmethod
    def invalidGuess(guess):
        """ Returns error message if guess is invalid or False if valid """
        guess = guess.lower()
        if not len(guess) == len(WordValidator.target):
            return WordValidator.INVALID_LENGTH
        if not guess.isalpha():
            return WordValidator.INVALID_CHARACTERS
        return False;
    
    @staticmethod
    def correctWord(guess):
        """ Returns if the guess matches the guesses word """
        return WordValidator.target == guess
    
    @staticmethod
    def validate(guess):
        """ Returns a string with the response to the guess
        Letters in the response correspond to the following circumstances
        U: Letter is higher in the alphabet
        D: Letter is lower
        R: Letter is within 5 of the guess to the right
        L: Ditto but left
        C: Letter is within 5 of guess in this spot
        X: Wrong!!! -- Allows computer to be a jerk on occasion
        Any lower-case letter is the correct letter in the correct spot """
        target = WordValidator.target
        response = ""
        l = []
        last = len(target)-1
        l.append(WordValidator.validateChar(guess[0], target[0], right=target[1]))              # Add first char
        for i in range(1, last):                                                                                          # Add middle chars    
            l.append(WordValidator.validateChar(guess[i], target[i], left=target[i-1], right=target[i+1]))
        l.append(WordValidator.validateChar(guess[last], target[last], left=target[last-1]))    # Add last char
        
        for char in l:
            response = response + char
        return response
        
    @staticmethod
    def validateChar(guess, target, left=None, right=None):
        """ Get the character in the response based on the target and guess chars """
        if WordValidator.match(guess, target):
            return target
            
        options = {}
        if WordValidator.up(guess, target):
            options["U"] = 3
        else:
            options["D"] = 3
            
        if WordValidator.close(guess, target):
            options["C"] = 5
        else:
            options["X"] = 2
            
        if left and WordValidator.close(guess, left):
            options["L"] = 2
        
        if right and WordValidator.close(guess, right):
            options["R"] = 2
            
        return WordValidator.probBuilder(options)
        
    @staticmethod
    def probBuilder(options):
        """ Returns a key in options randomly based on the value of each key
        Probability based on values """
        l = []
        for key in options:
            for x in range(options[key]):
                l.append(key)
                
        return random.choice(l)
            
            
    @staticmethod
    def match(guess, target):
        """ Checks if a guess letter matches a target letter """
        return guess == target
        
    @staticmethod
    def up(guess, target):
        """ Checks if a letter in a guess is above the target letter in the alphabet
        Return true if up, false is assumed to be down since this should never be 
        called if there is a match """
        return ord(target) < ord(guess)
        
    @staticmethod
    def close(guess, target):
        """ Check if the guess letter is within 5 letters of the target """
        return ord(target)-5 <= ord(guess) and ord(guess) <= ord(target)+5
    
        
    @staticmethod
    def nextWord():
        """ Moves validator to the next size of word or initializes if first time """
        if not WordValidator.target:
            WordValidator.target = WordChooser.pickWord(WordChooser.FIRSTLENGTH)
            return True
        
        if len(WordValidator.target) == WordChooser.MAXWORDLENGTH:
            return False
            
        WordValidator.target = WordChooser.pickWord(len(WordValidator.target)+1)
        WordValidator.INVALID_LENGTH = "Must be " + str(len(WordValidator.target)) + " characters long."
        return True
        