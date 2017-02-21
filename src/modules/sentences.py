"""generate a random combination of words"""
import sys
import random
import fileinput

import tokenization

def generate_sentence(words, length):
    """generates a sentence of the passed in length"""
    words_count = len(words)
    sentence = ""
    for _ in range(0, length):
        index = random.randint(1, words_count)
        count = 0
        for key in words:
            count += words[key]
            if count >= index:
                sentence += key
                sentence += ' ' #TODO: find better way
                break
    return sentence

if __name__ == '__main__':
    WORDS = tokenization.get_tokens_from_corpus('../input.txt')
    print generate_sentence(WORDS, int(sys.argv[1]))
