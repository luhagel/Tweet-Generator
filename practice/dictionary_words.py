"""generate a random combination of words"""
import sys
import random
import fileinput

def get_words():
    """populates the words array"""
    words = []
    for line in fileinput.input(['/usr/share/dict/words']):
        words += [line]
    return words

def generate_sentence(length):
    """generates a sentence of the passed in length"""
    WORDS = get_words()
    WORDS_COUNT = len(WORDS)

    sentence = ""
    for i in range(0, length):
        index = random.randint(0, WORDS_COUNT - 1)
        sentence += WORDS[index].rstrip() + ' '
    return sentence

if __name__ == '__main__':
    print generate_sentence(int(sys.argv[1]))
