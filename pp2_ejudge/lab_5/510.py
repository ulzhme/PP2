import re

s = input()
x = re.findall(r"cat|dog",s, re.IGNORECASE)
if x:
    print("Yes")
else:
    print("No")