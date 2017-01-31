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

def pick_random_word(arr):
    """takes an array, shuffles it and return the first element"""
    random.shuffle(arr)

    return arr[0]

def get_frequency(arr):
    """takes a string and calculates the frequency each word appears in it"""
    text = ' '.join(arr)
    hist = generate_histogram(text)
    for key in hist:
        print hist[key] / float(len(arr))



if __name__ == '__main__':
    WORDS = []
    for i in range(0, 10000):
        WORDS.append(pick_random_word(sys.argv[1:]))
    get_frequency(WORDS)
