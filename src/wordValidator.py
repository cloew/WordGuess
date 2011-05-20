from wordChooser import WordChooser

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
        
        return ""
        
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
        