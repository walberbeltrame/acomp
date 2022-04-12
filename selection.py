import numpy as np
from time import process_time_ns as ns

def sort(v):
  for j in range(len(v)-1,0,-1): #(1)
    i=0 #(2)
    for m in range(1,j+1): #(3)
      if v[m]>v[i]: #(4)
        i = m #(5)
      t = v[j] #(6)
      v[j] = v[i] #(7)
      v[i] = t #(8)

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