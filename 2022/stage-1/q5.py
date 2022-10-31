from numpy import *
from utils import *

# radii
r = pi**(-1/2)
s = 2**(-3/4)

c_2 = 2*s**2 - 2*s**2*cos(pi/4)
theta = arccos((2*r**2 - c_2) / (2*r**2))
area = r**2*(theta - sin(theta))/2

# submit
submit(area, 29388)