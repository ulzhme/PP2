import re

s = input()
t = input()

x = re.split(t, s)
for i in range(len(x)):
    if i == len(x)-1:
        print(x[i], end="")
    else: print(x[i], end = ",")