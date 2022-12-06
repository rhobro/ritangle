def to_base_n(n, base):
    if n == 0:
        return [0]
    
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return digits[::-1] # to big endian

i = 32
found = False
while not found:
    count = 0
    
    for base in range(2, i):
        # base expansion
        exp = to_base_n(i, base)
        
        if exp.count(1) == len(exp):
            count += 1
            
            # found
            if count == 3:
                print(i)
                found = True
                break
    
    i += 1