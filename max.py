import numpy as np
from time import process_time_ns as ns

def max(v):
  m = v[0] #(1)
  for i in range(1, len(v)): #(2)
    if v[i] > m: #(3)
      m = v[i] #(4)
  return m #(5)

v = np.random.randint(1, 10000, 10000)
s = sorted(v)
r = sorted(v, reverse=True)

n1 = ns()
m = max(s)
n2 = ns()

print(n2-n1)