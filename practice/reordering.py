import random
import sys

def reorder_args():
  args = []
  for arg in range(1, len(sys.argv) - 1):
    args += sys.argv[arg]
  return args

if __name__ == '__main__':
  print(reorder_args())
