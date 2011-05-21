import unittest

from wordValidator import WordValidator

class InvalidGuessTestCase(unittest.TestCase):
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
    
class CorrectWordTestCase(unittest.TestCase):
    def setUp(self):
        WordValidator.target = "sky"
        
    def testCorrectWord_correct(self):
        """ Recognize correct matches between target and guess """
        assert WordValidator.correctWord("sky") , "Should be the correct word"
        
    def testCorrectWord_incorrect(self):
        """ Recognize incorrect matches between target and guess  """
        WordValidator.correctWord("abc"),  "Should be incorrect word"
        
class CheckMatchTestCase(unittest.TestCase):
    def testCheckMatch_correct(self):
        """ Recognize a correct match of characters """
        assert WordValidator.match('a', 'a'), "Should be a match"
        
    def testCheckMatch_incorrect(self):
        """ Recognize an incorrect match of characters """
        assert not WordValidator.match('a', 'b'), "Should not be a match"
        
class CheckUpTestCase(unittest.TestCase):
    def testCheckUp_up(self):
        """ Recognize target character is up in the alphabet """
        assert WordValidator.up("b", "a"), "Should be up in the alphabet"
        
    def testCheckUp_down(self):
        """ Recognize target character is down in the alphabet """
        assert not WordValidator.up("a", "b"), "Should be down in the alphabet"
        
class CheckCloseTestCase(unittest.TestCase):
    def testCheckClose_closeUp(self):
        """ Recognize a character within 5 characters up of the target """
        assert WordValidator.close("a", "f"), "Should be close"
        
    def testCheckClose_closeDown(self):
        """ Recognize a character within 5 characters down of the target """
        assert WordValidator.close("f", "a"), "Should be close"
        
    def testCheckClose_notClose(self):
        """ Recognize a character within 5 characters down of the target """
        assert not WordValidator.close("a", "z"), "Should not be close"
        
if __name__ == "__main__":
    unittest.main()