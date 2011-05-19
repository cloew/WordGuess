import unittest

from wordValidator import WordValidator

class WordValidatorTest(unittest.TestCase):
    def setUp(self):
        self.word = "sky"
        WordValidator.target = "sky"

    def testValidateGuess_Valid_Lower(self):
        """ Recognize valid guesses with Lowercase letters """
        guess = self.word
        assert not WordValidator.invalidGuess(guess), "Should be valid guess"
        
    def testValidateGuess_Valid_Capitals(self):
        """ Recognize valid guesses with Capital letters """
        guess = self.word.upper()
        assert not WordValidator.invalidGuess(guess), "Should be valid guess"
    
    def testValidateGuess_Invalid_IncorrectLength(self):
        """ Recognize invalid guesses with incorrect length """
        guess = ""
        assert WordValidator.invalidGuess(guess) == WordValidator.INVALID_LENGTH, "Should be invalid guess - >invalid length"
        
   
    def testValidateGuess_Invalid_InvalidCharacters_Numbers(self):
        """ Recognize invalid guesses with numbers """
        guess = "sk1"
        assert WordValidator.invalidGuess(guess) == WordValidator.INVALID_CHARACTERS, "Should be invalid guess - >invalid characters(numbers)" 

    def testValidateGuess_Invalid_InvalidCharacters_Etc(self):
        """ Recognize invalid guesses with other characters """
        guess = "sk!"
        assert WordValidator.invalidGuess(guess) == WordValidator.INVALID_CHARACTERS, "Should be invalid guess - >invalid characters(etc)" 
                
                
if __name__ == "__main__":
    unittest.main()