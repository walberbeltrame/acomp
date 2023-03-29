def nove_r(n, d = 1):
  s = 0
  p = str(n)
  l = len(p)
  if l == 1:
      return [n == 9, d]
  else:
    for c in p:
      s += int(c)
    return nove_r(s, d+1)

def nove_i(n):
  d = 1
  p = str(n)
  l = len(p)
  while l > 1:
    s = 0
    for c in p:
      s += int(c)
    n = s
    d += 1
    p = str(s)
    l = len(p)
  return [n == 9, d]

r = nove_r(9)
print(r)
r = nove_r(99999999999999999999)
print(r)
r = nove_r(9999999999999999999999999999998)
print(r)
r = nove_i(9)
print(r)
r = nove_i(99999999999999999999)
print(r)
r = nove_i(9999999999999999999999999999998)
print(r)