import numpy as np
from time import process_time_ns as ns

def max(v):
  m = v[0]
  for i in range(1, len(v)):
    if v[i] > m:
      m = v[i]
  return m

v = np.random.randint(1, 100, 100)
s = sorted(v)
r = sorted(v, reverse=True)
n1 = ns()
max(v)
n2 = ns()
print(n2-n1)
n1 = ns()
max(s)
n2 = ns()
print(n2-n1)
n1 = ns()
max(r)
n2 = ns()
print(n2-n1)

v = np.random.randint(1, 1000, 1000)
s = sorted(v)
r = sorted(v, reverse=True)
n1 = ns()
max(v)
n2 = ns()
print(n2-n1)
n1 = ns()
max(s)
n2 = ns()
print(n2-n1)
n1 = ns()
max(r)
n2 = ns()
print(n2-n1)

v = np.random.randint(1, 10000, 10000)
s = sorted(v)
r = sorted(v, reverse=True)
n1 = ns()
max(v)
n2 = ns()
print(n2-n1)
n1 = ns()
max(s)
n2 = ns()
print(n2-n1)
n1 = ns()
max(r)
n2 = ns()
print(n2-n1)