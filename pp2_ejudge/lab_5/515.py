import re

s = input()
x = ""
start = 0
for i in range(len(s)):
    if (s[i].isdigit()):
        y = re.sub(s[i], 2*s[i], s[start:i+1])
        x += y
        start = i+1
    else:
        x += s[i]
        start+=1
print(x)