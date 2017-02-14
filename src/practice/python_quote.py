"""outputs a random monty python quote"""
import random

QUOTES = ("It's just  a flesh wound",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

def random_quote():
    """generate random index and return the corresponding quote"""
    rand_index = random.randint(0, len(QUOTES) - 1)
    return QUOTES[rand_index]

if __name__ == '__main__':
    QUOTE = random_quote()
    print QUOTE
