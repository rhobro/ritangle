def to_centi(s):
    return s/100

def merge_sort_sim(n, m):
    if m == 0:
        return to_centi(n*(n+1)/2)
    
    time1 = merge_sort_sim(n/2, m-1)
    time2 = merge_sort_sim(n/2, m-1)
    
    return time1+time2+to_centi(n+1)

shortest_m = 0
shortest = 999999999999
for m in range(1, 11):
    t = merge_sort_sim(1024, m)
    
    if t < shortest:
        shortest_m = m
        shortest = t

# submit
print(shortest+to_centi(1000))
print(shortest_m)