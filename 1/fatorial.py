def fatorial_r(n):
    if n == 0:
      return 1
    return n * fatorial_r(n - 1)

def fatorial_i(n):
  fatorial = 1
  while (n):
    fatorial *= n
    n -= 1
  return fatorial

n = fatorial_r(5)
print(n)
n = fatorial_i(5)
print(n)