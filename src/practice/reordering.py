"""Tweet Gen Challenges page 1"""
import random
import sys

def reorder_args():
    """reorder the arguments passed to the script"""
    args = []
    for arg in sys.argv:
        args += [arg]
    del args[0]

    random.shuffle(args)

    return args

if __name__ == '__main__':
    print reorder_args()
