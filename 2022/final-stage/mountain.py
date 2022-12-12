from numpy import *
from math import isqrt


# SPEED CONSTANTS CALCULATED
FLAT_SPEED = 2
DOWNHILL_SPEED = 3.2
UPHILL_SPEED = 0.8

       
class Mountain:
    def __init__(self, d):
        self.a = d["a"]
        self.b = d["b"]
        self.c = d["c"]
    
    # COORDINATE LOCATION
    @property
    def x(self):
        return self.a
    @property
    def y(self):
        return self.b
    @property
    def coords(self):
        return (self.x, self.y)
    # REAL WORLD COORDINATE LOCATION
    @property
    def real_x(self):
        return self.x * 1000.0
    @property
    def real_y(self):
        return self.y * 1000.0
    # DIMENSIONS
    @property
    def height(self):
        return self.c * 0.1875 * 1000.0
    @property
    def radius(self):
        return self.height/0.6
    
    """Pythagorean distance of mountain from coordinates"""
    def distance_from(self, x, y):
        return (
            (self.real_x - x)**2 + 
            (self.real_y - y)**2
        )**0.5
    
    """Pythagorean distance between mountains"""
    def distance_between(self, other):
        return self.distance_from(other.real_x, other.real_y)
    
    """Time taken to move from coordinates to mountain peak"""
    def time_from(self, x, y):
        r = self.radius
        flat = self.distance_from(x, y) - r
        
        return flat/FLAT_SPEED + r/UPHILL_SPEED
    
    """Time taken to move from mountain peak to coordinates"""
    def time_to(self, x, y):
        r = self.radius
        flat = self.distance_from(x, y) - r
        
        return r/DOWNHILL_SPEED + flat/FLAT_SPEED
    
    """Time taken to move between mountain peaks"""
    def time_between(self, other):
        r1 = self.radius
        r2 = other.radius
        dist = self.distance_between(other)
        
        overlap = r1 + r2 - dist
        if overlap < 0:
            # no overlap: flat = -overlap
            return r1/DOWNHILL_SPEED + r2/UPHILL_SPEED - overlap/FLAT_SPEED
        
        downhill = r1 - overlap/2
        uphill = r2 - overlap/2
        if downhill < 0 or uphill < 0:
            # engulfed
            return inf
        
        return downhill/DOWNHILL_SPEED + uphill/UPHILL_SPEED
    
    """Brute force search for all mountains satisfying a^2 + b^2 + c^2 = 734"""
    def find_all(r=30):  
        mountains = []

        for a in range(r):
            for b in range(r):
                c_2 = 734 - a**2 - b**2
                if c_2 < 0:
                    continue
                
                if is_square(c_2):
                    mountains.append(Mountain({
                        "a": a,
                        "b": b,
                        "c": int(sqrt(c_2)),
                    }))
        
        return mountains

def is_square(n):
    return n == isqrt(n)**2