import numpy as np
from time import process_time_ns as ns

def sort(v):
    return

def main(*args):
  v = np.random.randint(1, 100, 100)
  # s = sorted(v)
  # r = sorted(v, reverse=True)

  print(v)
  
  n1 = ns()
  sort(v)
  n2 = ns()

  print(v)
  print(n2-n1)

if __name__ == '__main__':
    main()