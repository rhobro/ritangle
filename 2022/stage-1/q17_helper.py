for a in range(1, 50):
    for b in range(1, 50-a):
        c = 51 - a - b
        
        sq = a**2 + b**2 + c**2
        sa = a*b + b*c + c*a
        if sq == 899 and sa == 851:
            print(a, b, c)
            break