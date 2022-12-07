from numpy import *
import sympy as sym

def concat(a, b):
  return int(str(a) + str(b))
def n_digits(n):
  return ceil(log10(n))
  
cs = []

for b in range(1, 1000):
  for a in range(b+1, 1001):
    c = concat(a-b, a+b)
    
    if n_digits(c) == 5:
      if sym.isprime(c):
        cs.append(c)

print(min(cs))