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
        if b >= e: #(1)
            return
        p = partition(v, b, e) #(2)
        _sort(v, b, p-1) #(3)
        _sort(v, p+1, e) #(4)
    return _sort(v, b, e)

def main(*args):
  v = np.random.randint(1, 100, 100)
  s = sorted(v)
  r = sorted(v, reverse=True)
  
  n1 = ns()
  sort(v)
  n2 = ns()
  print(n2-n1)

  n1 = ns()
  sort(s)
  n2 = ns()
  print(n2-n1)

  n1 = ns()
  sort(r)
  n2 = ns()
  print(n2-n1)

if __name__ == '__main__':
    main()