import random

class WordChooser:
    """ Chooses Word for current level of WordGuess """
    words = {}
    words[3] = ["any", "bye", "say", "day", "lie", "dye", "ski", "fly"]
    
    MAXWORDLENGTH = 3
    
    @staticmethod
    def pickWord(length):
        """ Picks a word with the given length """
        return random.choice(WordChooser.words[length])
        
      