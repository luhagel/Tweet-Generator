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
    """takes a histgram and return the number of unique words"""
    return len(histogram)

if __name__ == '__main__':
    FISH = generate_histogram("one fish two fish red fish blue fish")
    print FISH
    print unique_words(FISH)
