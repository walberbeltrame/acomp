import numpy as np
from time import process_time_ns as ns

def sort(v):
  for i in range(1,len(v)): #(1)
    c = v[i] #(2)
    p = i #(3)
    while p>0 and v[p-1]>c: #(4)
      v[p] = v[p-1] #(5)
      p = p-1 #(6)
    v[p]=c #(7)

def main(*args):
  v = np.random.randint(1, 100, 100)
  # s = sorted(v)
  # r = sorted(v, reverse=True)

  n1 = ns()
  sort(v)
  n2 = ns()

  print(v)
  print(n2-n1)

if __name__ == '__main__':
    main()