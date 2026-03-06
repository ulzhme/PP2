import re

s = input()
x = re.compile(r'\b\w+\b')
w = x.findall(s)
print(len(w))