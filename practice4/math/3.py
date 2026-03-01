# 3 (Calculate the area of a regular polygon)
import math

n = 4   # number of sides
s = 25  # length of a side

area = (n * s**2) / (4 * math.tan(math.pi / n))
print("Input number of sides:", n)
print("Input the length of a side:", s)
print("The area of the polygon is:", area)