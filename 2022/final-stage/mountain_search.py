from numpy import *
import json
        
mountains = []

for a in range(29):
    for b in range(29):
        c2 = 734 - a**2 - b**2
        if c2 < 0:
            continue
        
        c = c2**0.5
        if c == int(c):
            mountains.append({
                "x": a,
                "y": b,
                "height": c * 0.1875,
            })

# where closer than 28km
mountains = [m for m in mountains if m["x"]**2 + m["y"]**2 <= 784]

with open("mountains.json", "w") as f:
    f.write(json.dumps(mountains, indent=4*" "))