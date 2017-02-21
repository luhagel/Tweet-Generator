"""tokenize corpus"""
import string

import modules.histogram

def trim_punctuation_from_word(word):
    """strip punctuation from input word"""
    char_list = []
    for char in word:
        if char not in string.punctuation:
            char_list.append(char)
    trimmed_word = ''.join(char_list)
    return trimmed_word

def trim_punctuation(raw_word_list):
    """strip punctuation from input word list"""
    word_list = []
    for word in raw_word_list:
        trimmed_word = trim_punctuation_from_word(word)
        if len(trimmed_word) > 0:
            word_list.append(trimmed_word)
    return word_list

def get_raw_words_from_file(filename):
    """open supplied file and return a list of raw words"""
    with open(filename) as opened_file:
        corpus = opened_file.read()

    word_list = corpus.split()
    return word_list

def get_tokens_from_corpus(filename):
    """see function name"""
    token_gram = modules.histogram.Histogram(trim_punctuation(get_raw_words_from_file(filename)))
    return token_gram
