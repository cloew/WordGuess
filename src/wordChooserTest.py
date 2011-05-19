import unittest

from wordChooser import WordChooser

class WordChooserTest(unittest.TestCase):
    def runTest(self):
        word = WordChooser.pickWord(WordChooser.MAXWORDLENGTH)
        assert word in WordChooser.words[WordChooser.MAXWORDLENGTH],  "Didn't return a word in the correct location"
                
                
if __name__ == "__main__":
    unittest.main()