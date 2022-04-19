import numpy as np
from time import process_time_ns as ns

def partition(v, b, e):
    p = b
    for i in range(b+1, e+1):
        if v[i] <= v[b]:
            p += 1
            v[i], v[p] = v[p], v[i]
    v[p], v[b] = v[b], v[p]
    return p

def sort(v, b=0, e=None):
    if e is None:
        e = len(v) - 1
    def _sort(v, b, e):
        if b >= e:
            return
        p = partition(v, b, e)
        _sort(v, b, p-1)
        _sort(v, p+1, e)
    return _sort(v, b, e)

def main(*args):
  v = np.random.randint(1, 100, 100)
  # s = sorted(v)
  # r = sorted(v, reverse=True)
  
  n1 = ns()
  sort(v)
  n2 = ns()

  print(n2-n1)

if __name__ == '__main__':
    main()