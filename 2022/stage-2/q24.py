ms = []

for u1 in range(100):
    for u2 in range(100):
        
        un = u2
        un_m1 = u1
        i = 3
        while True:
            nxt = abs(un) - un_m1
            if nxt == u1:
                ms.append(i)
                break
            
            un_m1 = un
            un = nxt
            i += 1
            
print(max(ms))