import numpy as np
from time import process_time_ns as ns

def merge(lp, lr):
    v = [] #(1)
    i = j = 0 #(1)
    while i < len(lp) and j < len(lr): #(2)
        if lp[i] < lr[j]: #(3)
            v.append(lp[i]) #(4)
            i += 1 #(5)
        else:
            v.append(lr[j]) #(4)
            j += 1 #(5)
    v.extend(lp[i:]) #(6)
    v.extend(lr[j:]) #(7)
    return v #(8)

def sort(v):
    l = len(v) #(1)
    if l == 1: #(2)
        return v #(3)
    m = l // 2 #(4)
    lp = sort(v[:m]) #(5)
    rp = sort(v[m:]) #(6)
    return merge(lp, rp) #(7)

def main(*args):
  v = np.random.randint(1, 100, 100)
  # s = sorted(v)
  # r = sorted(v, reverse=True)
  
  n1 = ns()
  v = sort(v)
  n2 = ns()

  print(n2-n1)

if __name__ == '__main__':
    main()