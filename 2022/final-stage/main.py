from numpy import *
import pandas as pd
from mountain import *
from display import *


def main():
    # list mountains
    mountains = Mountain.find_all()
    
    # initialise cost matrix
    costs = CostMatrix()
    for m1 in mountains:
        for m2 in mountains:
            costs.set(m1.coords, m2.coords, m1.time_between(m2))
    
    # find naïve shortest path for all mountains 
    l_cost = inf
    l_path = None
    
    for m in mountains:
        # for lower half diagonal to avoid duplication
        if m.coords[0] < m.coords[1]:
            continue
        
        # naïve shortest
        stack, cost = costs.shortest([m.coords])
        # identify closest coast points
        start = closest_coast(stack[0])
        stack.insert(0, start)
        end = closest_coast(stack[-1])
        stack.append(end)
        # add cost from points
        cost += m.time_from(start[0], start[1])
        cost += m.time_to(end[0], end[1])
        
        if cost < l_cost:
            l_cost = cost
            l_path = stack
    
    display(l_cost, mountains, l_path)
    
    
class CostMatrix:
    def __init__(self):
        self.m = {}
        
    def set(self, k1, k2, cost):
        if k1 not in self.m.keys():
            self.m[k1] = {}
        self.m[k1][k2] = cost
    
    def get(self, k1, k2):
        return self.m[k1][k2]
    
    def next_possible(self, k1, exclude=[]):
        nodes = [k for k in self.m[k1] if self.m[k1][k] != inf and k not in exclude]
        costs = [self.get(k1, n) for n in nodes]
        return pd.DataFrame({
            "next": nodes,
            "costs": costs
        })
    
    @property
    def size(self):
        return len(self.m)
        
    def shortest(self, stack):
        nexts = self.next_possible(stack[-1], stack).sort_values("costs")
        next_coords = nexts.next.tolist()

        # nowhere else to go
        if nexts.shape[0] == 0:
            # incomplete
            if len(stack) != self.size:
                return stack, inf

            total = 0
            for i in range(len(stack)-1):
                total += self.get(stack[i], stack[i+1])
            return stack[:], total

        stack.append(next_coords[0])
        rs = self.shortest(stack)
        stack.pop()

        return rs

coast = [
    (27, 0),
    (27, 3),
    (27, 4),
    (27, 5),
    (27, 6),
    (27, 7),
    (26, 8),
    (26, 9),
    (26, 10),
    (25, 11),
    (25, 12),
    (24, 12),
    (24, 13),
    (24, 14),
    (23, 15),
    (22, 16),
    (22, 17),
    (21, 18),
    (20, 18),
    (20, 19),
    
    (19, 19),
    
    (0, 27),
    (3, 27),
    (4, 27),
    (5, 27),
    (6, 27),
    (7, 27),
    (8, 26),
    (9, 26),
    (10, 26),
    (11, 25),
    (12, 25),
    (12, 24),
    (13, 24),
    (14, 24),
    (15, 23),
    (16, 22),
    (17, 22),
    (18, 21),
    (18, 20),
    (19, 20)
]

def closest_coast(c):
    l_coast = None
    l_cost2 = inf
    
    for point in coast:
        d2 = (point[0]-c[0])**2 + (point[1]-c[1])**2
        if d2 < l_cost2:
            l_cost2 = d2
            l_coast = point
        
    return l_coast

def display(cost, mountains, path = None, plot=True):
    print(cost)
    if path is not None:
        for p in path:
            print(f"{p[0]},{p[1]}")

    if plot:
        show_it(mountains, path)

if __name__ == "__main__":
    main()
