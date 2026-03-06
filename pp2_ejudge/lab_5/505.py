import re

s = input()
start = re.findall("^[a-zA-Z_]", s)
end = re.findall("[0-9]$", s)
if start and end:
    print("Yes")
else: print("No")