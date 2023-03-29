def joseph_r(n, m, l=list()):
  if not l:
    l = list(range(1, n+1))
  if len(l) == 1:
    return l[0]
  n = (n + m - 1) % len(l)
  l.pop(n)
  return joseph_r(n, m, l)

def joseph_i(n, m):
  l = list(range(1, n+1))
  while len(l) > 1:
    n = (n + m - 1) % len(l)
    l.pop(n)
  return l[0]

def joseph_k(k, m=1):
  v = 0
  n = 2*k
  l = list(range(1, n+1))
  n = (n + m - 1) % len(l)
  while l[n] > k:
    v += 1
    l.pop(n)
    n = (n + m - 1) % len(l)
  if v == k:
    return m
  else:
    return joseph_k(k, m+1)

r = joseph_r(6, 5)
print(r)

r = joseph_i(6, 5)
print(r)

r = joseph_k(3)
print(r)

r = joseph_k(4)
print(r)