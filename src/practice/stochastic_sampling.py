"""stochastic sampling challenge"""
import sys
import random

def generate_histogram(text):
    """genereate a histogram"""
    histogram = {}
    words = text.split()
    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else:
            histogram[word] = 1
    return histogram

############################################

WORDS_COUNT = 0

def pick_random_word(arr):
    """takes an array, shuffles it and return the first element"""
    random.shuffle(arr)

    return arr[0]

def get_frequency(arr):
    """takes a string and calculates the frequency each word appears in it"""
    text = ' '.join(arr)
    hist = generate_histogram(text)
    for key in hist:
        print  key + ' -> ' + str(hist[key] / float(len(arr)))

def get_words_count(dict):
    """returns the wordcount in a histogramm"""
    count = 0
    for key in dict:
        count += dict[key]
    return count

def pick_weighted_random_word(dict):
    """takes a histogram and returns a random word, weighted by the frequency"""
    index = random.randint(1, WORDS_COUNT)
    count = 0
    for key in dict:
        count += dict[key]
        if count >= index:
            return key

# -----MAIN-----

if __name__ == '__main__':
    WORDS = []
    WEIGHTED_WORDS = []

    INPUT_TEXT = ' '.join(sys.argv[1:])
    INPUT_HISTOGRAM = generate_histogram(INPUT_TEXT)
    WORDS_COUNT = get_words_count(INPUT_HISTOGRAM)
    print WORDS_COUNT

    for i in range(0, 10000):
        WORDS.append(pick_random_word(sys.argv[1:]))
    get_frequency(WORDS)
    print '--------------------------------------------'
    for i in range(0, 10000):
        WEIGHTED_WORDS.append(pick_weighted_random_word(INPUT_HISTOGRAM))
    get_frequency(WEIGHTED_WORDS)
