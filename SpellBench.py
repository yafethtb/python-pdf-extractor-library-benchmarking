from textblob import TextBlob
import string

class SpellBenchmark:
    def __init__(self, sentences) -> None:
        self.cleanword = sentences.translate(str.maketrans('', '', string.punctuation)).lower()
        self.wordlist = [word for word in self.cleanword.split(' ') if word != '']
        self.wordcount = len(self.wordlist)
        self.misscount = self.miss_count()
        self.accuracy = self.accuracy_count()

    def miss_count(self):
        """Counting how much misspelling in text."""
        count = 0
        for word in self.wordlist:
            blob = TextBlob(word).correct()    
            if word != blob:
                count += 1
        return count
    
    def accuracy_count(self):
        """Calculate spelling accuracy of text."""
        misspct= (self.misscount/self.wordcount) * 100
        return 100 - misspct