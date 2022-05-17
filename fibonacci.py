import numpy as np
import math as mt
from time import process_time_ns as ns

def fib_2n(n):
  if n == 0: #(1)
    return 0
  elif n == 1: #(2)
    return 1
  else:
    return fib_2n(n-1) + fib_2n(n-2) #(3)

def fib_n(n):
  a = 0
  b = 1
  for i in range(2, n + 1): #(1)
    c = a #(2)
    a = b #(3)
    b = c + b #(4)
  return b if n > 0 else 0

def fib_lgn(n):
  m = np.array([[1, 1], [1, 0]])
  return np.linalg.matrix_power(m, n)[0][1] #(1)

sqrt5 = mt.sqrt(5)
phi = (1+sqrt5)/2
def fib_1(n):
  return int((mt.pow(phi,n)-mt.pow(-phi,-n))/sqrt5) #(1)

def main(*args):

  n = 100
  
  n1 = ns()
  fib_2n(6)
  n2 = ns()
  print(n2-n1)

  n1 = ns()
  fib_n(n)
  n2 = ns()
  print(n2-n1)

  n1 = ns()
  fib_lgn(n)
  n2 = ns()
  print(n2-n1)

  n1 = ns()
  fib_1(n)
  n2 = ns()
  print(n2-n1)

if __name__ == '__main__':
    main()