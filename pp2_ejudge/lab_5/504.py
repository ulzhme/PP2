import re

s = input()

for m in re.finditer(r"\d", s):
    print(m.group(), end=" ")