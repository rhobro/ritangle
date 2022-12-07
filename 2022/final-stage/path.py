from numpy import *
import json

FLAT_SPEED = 2
DOWNHILL_SPEED = 3.2
UPHILL_SPEED = 0.8
        
class Mountain:
    def __init__(self, d):
        self.x = d["x"]
        self.y = d["y"]
        self.height = d["height"]
    
    def norm(self):
        return (self.x**2 + self.y**2)**0.
    
    def distance_from(self, other):
        return (1e6*((self.x-other.x)**2 + (self.y-other.y)**2))**0.5

class Node:
    def __init__(self, m):
        self.m = m
        self.cost = inf
        self.previous = None

# ALPHA = -arctan(-3/5)
def mountain_radius(h):
    # h/tan(ALPHA)
    return h/0.6

def time_between(n1, n2):
    r1 = mountain_radius(n1.m.height)
    r2 = mountain_radius(n2.m.height)
    flat_distance = n1.m.distance_from(n2.m) - r1 - r2
    if flat_distance < 0:
        return inf
    
    return r1/DOWNHILL_SPEED + r2/UPHILL_SPEED + flat_distance*FLAT_SPEED

start = (27, 1)
ends = [
    (27, 1),
    (26, 7),
    (25, 10),
    (23, 13),
    (23, 14),
    (22, 15),
    (21, 17),
    (19, 18)
]
end = (27, 1)


with open("mountains.json") as f:
    mountains = json.loads(f.read())
# filter lower half
mountains = [u for u in mountains if u["x"] > u["y"]]
unvisited = {}
for u in mountains:
    node = Node(Mountain(u))
    unvisited[(node.m.x, node.m.y)] = node
# mark start
unvisited[start].cost = 0

def lowest_cost(ls):
    l_coords = None
    l_cost = inf
    
    for coords in ls:
        node = ls[coords]
        
        if node.cost < l_cost:
            l_cost = node.cost
            l_coords = coords
    return l_coords

visited = {}
while len(unvisited) > 0:
    current_c = lowest_cost(unvisited)
    for dst_c in unvisited:
        if dst_c == current_c:
            continue
        
        cost = time_between(unvisited[current_c], unvisited[dst_c])
        if cost < unvisited[dst_c].cost:
            unvisited[dst_c].cost = cost
            unvisited[dst_c].previous = current_c
    visited[current_c] = unvisited.pop(current_c)