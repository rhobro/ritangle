from utils import *
from math import *

c_2 = 1 + 1 - 2*cos(radians(100))
a_2 = c_2 / (5 - 4*cos(radians(130)))

theta = acos((2 - a_2) / 2) / 2
theta = degrees(theta)

# submit
submit(theta, 2.23)