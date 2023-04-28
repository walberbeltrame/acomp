import numpy as np
from time import process_time_ns as ns

def fa(n):
  s = 0
  for i in range(0, n):
    for j in range(i+1, n + 1):
      for k in range(1, j + 1):
        s = 1
  return s

def fb(n):
  s = 0
  for i in range(1, n):
    for j in range(1, 2*n):
      s = s + 1
  return s

def fc(v):
  n = len(v)
  m = v[0]
  for i in range(1, n+1, 2):
    for j in range(n-i, 0, -1):
      if v[i] < v[j]:
        m = v[i]
  return m

n1 = ns()
fa(100)
n2 = ns()
print(n2-n1)

n1 = ns()
fb(100)
n2 = ns()
print(n2-n1)

v = np.random.randint(1, 100, 100)
s = sorted(v)
n1 = ns()
fc(s)
n2 = ns()
print(n2-n1)

n1 = ns()
fa(1000)
n2 = ns()
print(n2-n1)

n1 = ns()
fb(1000)
n2 = ns()
print(n2-n1)

v = np.random.randint(1, 1000, 1000)
s = sorted(v)
n1 = ns()
fc(s)
n2 = ns()
print(n2-n1)

n1 = ns()
fb(10000)
n2 = ns()
print(n2-n1)

v = np.random.randint(1, 10000, 10000)
s = sorted(v)
n1 = ns()
fc(s)
n2 = ns()
print(n2-n1)