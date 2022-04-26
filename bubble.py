import numpy as np
from time import process_time_ns as ns

def sort(v):
  for j in range(len(v)-1,0,-1): #(1)
    for i in range(j): #(2)
      if v[i]>v[i+1]: #(3)
        t = v[i] #(4)
        v[i] = v[i+1] #(5)
        v[i+1] = t #(6)

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