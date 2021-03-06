import random

class WordChooser:
    """ Chooses Word for current level of WordGuess """
    words = {}
    words[2] = ["at", "as", "it", "by", "hi", "up", "on", "in", "of", "my", "no"]
    words[3] = ["any", "bye", "say", "day", "lie", "dye", "ski", "fly", "egg", "not", "yes"]
    
    FIRSTLENGTH = 2
    MAXWORDLENGTH = 6
    
    @staticmethod
    def loadWords(path):
        """ Sets up the set of words """
        for file in range(WordChooser.FIRSTLENGTH, WordChooser.MAXWORDLENGTH+1):
            f = None
            try:
                f = open("%swords/%d" % (path, file), 'r')
                WordChooser.words[file] = []
                for line in f:
                    WordChooser.words[file].append(line.strip())
            except IOError:
                print "Unable to retrieve %d character-long words" % file
                exit(-1)
            finally:
                if f:
                    f.close()
                
    
    @staticmethod
    def pickWord(length):
        """ Picks a word with the given length """
        return random.choice(WordChooser.words[length])