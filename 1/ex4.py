from itertools import permutations

def busca_r(v, s, i=0):
  if i == len(v):
    return -1
  if v[i] == s:
    return i + 1
  return busca_r(v, s, i + 1)

def busca_i(v, s):
  for i, p in enumerate(v):
    if p == s:
      return i + 1
  return -1

def procura(b, s):
  v = [str().join(p) for p in list(permutations(list(s)))]
  v = sorted([*set(v)])
  return b(v, s)

s = 'bacaa'
r = procura(busca_r, s)
print(r)
r = procura(busca_i, s)
print(r)

s = 'abc'
r = procura(busca_r, s)
print(r)
r = procura(busca_i, s)
print(r)

s = 'cba'
r = procura(busca_r, s)
print(r)
r = procura(busca_i, s)
print(r)