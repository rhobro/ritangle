from itertools import permutations as perms
from math import prod
from utils import *

DIGITS = list("123456")

# all combinations of digits
combs = perms(DIGITS)

# parses combination into numbers
def transform(comb):
    a = int(comb[0] + comb[1])
    b = int(comb[2] + "5" + comb[3])
    c = int(comb[4] + "4" + comb[5])
    
    return a, b, c

# mapping function to check common difference
def is_valid(comb):
    a, b, c = transform(comb)
    return c-b == b-a

combs = [comb for comb in combs if is_valid(comb)]  # apply filter
combs = [transform(comb) for comb in combs]  # transform valid combos
products = [prod(c) for c in combs] # product of each combo
ans = max(products) # select max

# submit
submit(ans, 3.8e-6)