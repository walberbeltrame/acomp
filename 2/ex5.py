import random
import string
from time import process_time_ns as ns

def ma(s, p):
  ns = len(s)
  np = len(p)
  f = False
  i = 0
  for i in range(ns-np+1):
    j = 0
    for j in range(np):
      if s[i+j] != p[j]:
        break
    if j == np - 1:
      f = True
      break
  if f:
    return i
  else:
    return -1

# KMP Algorithm
def mb(s, p):
  m = len(s)
  n = len(p)
  l = [0]*m
  j = 0
  lps(s, m, l)
  i = 0
  while (n - i) >= (m - j):
    if s[j] == p[i]:
      i += 1
      j += 1
    if j == m:
      return str(i-j)
      j = l[j-1]
    elif i < n and s[j] != p[i]:
      if j != 0:
        j = l[j-1]
      else:
        i += 1

def lps(s, m, l):
    len = 0
    l[0] = 0
    i = 1
    while i < m:
      if s[i] == s[len]:
        len += 1
        l[i] = len
        i += 1
      else:
        if len != 0:
          len = l[len-1]
        else:
          l[i] = 0
          i += 1

def gz(s, z):
  n = len(s)
  l, r, k = 0, 0, 0
  for i in range(1, n):
    if i > r:
      l, r = i, i
      while r < n and s[r - l] == s[r]:
        r += 1
      z[i] = r - l
      r -= 1
    else:
      k = i - l
      if z[k] < r - i + 1:
        z[i] = z[k]
      else:
        l = i
        while r < n and s[r - l] == s[r]:
          r += 1
        z[i] = r - l
        r -= 1

def mc(s, p):
  c = p + "$" + s
  l = len(c)
  z = [0] * l
  gz(c, z)
  for i in range(l):
    if z[i] == len(p):
      return (i-len(p)-1)

s=''.join(random.choices(string.ascii_lowercase, k=100))
a=''.join(random.choices(string.ascii_lowercase, k=10))
n1 = ns()
ma(s,a)
n2 = ns()
print(n2-n1)

n1 = ns()
mb(s,a)
n2 = ns()
print(n2-n1)

n1 = ns()
mc(s,a)
n2 = ns()
print(n2-n1)

s=''.join(random.choices(string.ascii_lowercase, k=1000))
a=''.join(random.choices(string.ascii_lowercase, k=100))
n1 = ns()
ma(s,a)
n2 = ns()
print(n2-n1)

n1 = ns()
mb(s,a)
n2 = ns()
print(n2-n1)

n1 = ns()
mc(s,a)
n2 = ns()
print(n2-n1)

s=''.join(random.choices(string.ascii_lowercase, k=10000))
a=''.join(random.choices(string.ascii_lowercase, k=1000))
n1 = ns()
ma(s,a)
n2 = ns()
print(n2-n1)

n1 = ns()
mb(s,a)
n2 = ns()
print(n2-n1)

n1 = ns()
mc(s,a)
n2 = ns()
print(n2-n1)