import re

s = input()
t = input()

x = re.escape(t)
y = re.findall(x, s)
print(len(y))