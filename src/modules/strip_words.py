import string

def trim_punctuation_from_word(word):
    char_list = []
    for char in word:
        if char not in string.punctuation:
            char_list.append(char)
    trimmed_word = ''.join(char_list)
    return trimmed_word

def trim_punctuation(word_list):
    word_list = []
    for word in word_list:
        trimmed_word = trim_punctuation_from_word(word)
        if len(trimmed_word) > 0:
            word_list.append(trimmed_word)
    return word_list
