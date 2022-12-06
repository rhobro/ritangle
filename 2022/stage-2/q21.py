import sympy as sym
from math import prod

def digit_sum(n):
    return sum([int(d) for d in str(n)])
def digit_prod(n):
    return prod([int(d) for d in str(n)])

def is_a_prime(p):
    next = sym.nextprime(p)
    return next - p == digit_sum(p)
def is_m_prime(p):
    next = sym.nextprime(p)
    return next - p == digit_prod(p)
def is_am_prime(p):
    next = sym.nextprime(p)
    return next - p == digit_sum(p) + digit_prod(p)

i = 2
while True:
    if is_am_prime(i):
        if not is_a_prime(i):
            print(i)
            break
            
    i = sym.nextprime(i)