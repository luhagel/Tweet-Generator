"""histogram challenge"""

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

def unique_words(histogram):
    """takes a histgram and returns the number of unique words"""
    return len(histogram)

def frequency(histogram, word):
    """takes a histgram and a word and returns the number of times the word appeared"""
    if word in histogram:
        return histogram[word]
    else:
        return 0

if __name__ == '__main__':
    FISH = generate_histogram("one fish two fish red fish blue fish")
    print FISH
    print unique_words(FISH)
    print frequency(FISH, 'fish')
