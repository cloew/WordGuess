from wordChooser import WordChooser

class WordValidator:
    """ Validates a guess related to the answer """
    
    INVALID_LENGTH = "Must be " + str(WordChooser.FIRSTLENGTH) + " characters long."
    INVALID_CHARACTERS = "Guess can only conatin alphabet characters"
    word = None
    
    @staticmethod
    def invalidGuess(guess):
        """ Returns error message if guess is invalid or False if valid """
        guess = guess.lower()
        if not len(guess) == len(WordValidator.word):
            return WordValidator.INVALID_LENGTH
        if not guess.isalpha():
            return WordValidator.INVALID_CHARACTERS
        return False;
        
    @staticmethod
    def nextWord():
        """ Moves validator to the next size of word or initializes if first time """
        if not WordValidator.word:
            WordValidator.word = WordChooser.pickWord(WordChooser.FIRSTLENGTH)
            return True
        
        if len(WordValidator.word) == WordChooser.MAXWORDLENGTH:
            return False
            
        WordValidator.word = WordChooser.pickWord(len(WordValidator.word)+1)
        