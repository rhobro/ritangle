import json

def main():
    # load cipher grid
    grid = CipherGrid("cipher.json")
    
    # load stage 1 solutions
    with open("../stage-1/codes.json", "r") as f:
        sols = json.loads(f.read())
        
    # factorise each
    # this leaves all 2s and 3s
    sols = [factorise(n) for n in sols]
    
    # count 2s and 3s as coordinates
    sols = [(n.count(2), n.count(3)) for n in sols]
    
    # decode coordinates on cipher grid
    sols = [grid.decode(x, y) for x, y in sols]
    
    # concat
    message = "".join(sols)
    print(message)


class CipherGrid:
    def __init__(self, path):
        # JSON grid structured already into indices
        with open("cipher.json") as f:
            self.grid = json.loads(f.read())
    
    def decode(self, x, y):
        return self.grid[x][y]


# brute force factorisation - ok for small numbers
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


if __name__ == "__main__":
    main()