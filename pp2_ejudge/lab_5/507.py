import re

s = input()
t = input()
r = input()

x = re.sub(t, r, s)
print(x)