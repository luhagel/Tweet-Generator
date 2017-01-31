"""generate a random combination of words"""
import sys
import random
import fileinput
from datetime import datetime
START_TIME = datetime.now()

def get_words():
    """populates the words array"""
    words = []
    for line in fileinput.input(['/usr/share/dict/words']):
        words += [line]
    return words

def generate_sentence(words, length):
    """generates a sentence of the passed in length"""
    words_count = len(words)
    sentence = ""
    for _ in range(0, length):
        index = random.randint(0, words_count - 1)
        sentence += words[index].rstrip() + ' '
    return sentence

if __name__ == '__main__':
    WORDS = get_words()
    print generate_sentence(WORDS, int(sys.argv[1]))
    print "Generating the sentence took " + str(datetime.now() - START_TIME)
