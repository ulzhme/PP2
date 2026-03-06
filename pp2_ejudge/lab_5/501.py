import re

s = input()
math = re.match("Hello", s)
if math:
    print("Yes")
else:
    print("No")