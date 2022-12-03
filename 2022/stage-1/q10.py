from itertools import permutations as perms

DIGITS = "123456789"

combs = perms(DIGITS)

def transform(comb):
    a = float("".join(comb[:3]))
    b = float("".join(comb[3:6]))
    c = float("".join(comb[6:]))
    return a, b, c

combs = [transform(c) for c in combs]

def heron(c):
    return (
        (c[0] + c[1] + c[2]) * \
        (-c[0] + c[1] + c[2]) * \
        (c[0] + -c[1] + c[2]) * \
        (c[0] + c[1] + -c[2])
    )**(1/2) / 4

combs = [heron(c) for c in combs]
combs = [c for c in combs if type(c) != complex and c != 0]

p = max(combs)
q = min(combs)
ans = round(p/q)

# submit
print(ans)