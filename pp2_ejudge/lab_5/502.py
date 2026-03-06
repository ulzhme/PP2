import re

s = input()
t = input()
math = re.search(t, s)
if math:
    print("Yes")
else:
    print("No")