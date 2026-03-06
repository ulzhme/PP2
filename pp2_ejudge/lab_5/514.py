import re

s = input()
match = re.compile(r'[0-9]')
x = match.findall(s)
if (len(x) == len(s)):
    print("Match")
else:
    print("No match")