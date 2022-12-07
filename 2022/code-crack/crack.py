import json

# load cipher grid
with open("cipher.json") as f:
    grid = json.loads(f.read())
def decipher(x, y):
    return grid[x][y]

# solutions
ns = [
    int(n)
    for n in 
    "18 648 27 324 432 6 72 36 81 8 108 16 54 48 9 24 12 2 144 3".split()
]

def factorise(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# factorise each
ns = [factorise(n) for n in ns]
# count 2s and 3s into coordinates
ns = [(n.count(2), n.count(3)) for n in ns]
# decipher
ns = [decipher(n[0], n[1]) for n in ns]
# concat
message = "".join(ns)

print(message)