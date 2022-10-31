from itertools import permutations as perms
from utils import *

DIGITS = list("12346789") # exclude 0, 5

# all combinations of digits
combs = list(perms(DIGITS))

# insert 0 and 5 in predefined places
for i, c in enumerate(combs):
    comb = list(c)
    comb.insert(4, "5")
    comb.append("0")
    combs[i] = comb

# concat
combs = ["".join(c) for c in combs]

# mapping validation function
def is_valid(c):
    for ith in [2, 3, 4, 6, 7, 8, 9]: # exclude 1, 5 and 10
        if int(c[:ith]) % ith != 0:
            return False
    return True

combs = [c for c in combs if is_valid(c)]  # apply filter
ans = int(combs[0])

# submit
submit(ans, 1.7e-7)