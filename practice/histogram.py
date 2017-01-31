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

if __name__ == '__main__':
    print generate_histogram("one fish two fish red fish blue fish")
