from math import floor, sqrt, sin, pi

a = 2/sqrt(sqrt(3))
ans = a/sqrt(2) - a*sin(pi/12)

print(f"Answer: {ans}")
print(f"Code: {floor(ans * 476)}")