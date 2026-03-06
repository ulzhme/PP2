import re

s = input()
t = input()
math = re.findall(t, s)
print(len(math))