def perm_r(s):
  if(len(s) == 1):
    return [s]
  v = []
  for i, c in enumerate(s):
    v += [c+p for p in perm_r(s[:i] + s[i+1:])]
  return sorted(v)

def perm_i(s):
  v = []
  v.append(s[0])
  for i in range(1, len(s)):
    for j in reversed(range(len(v))):
      t = v.pop(j)
      for k in range(len(t) + 1):
        v.append(t[:k] + s[i] + t[k:])
  return sorted(v)

r = perm_r('bca')
print(r)

r = perm_i('bca')
print(r)