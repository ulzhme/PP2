import re

s = input()
pat = re.compile(r'^\S+@\S+\.\S+$')
lines = s.split()

for line in lines:
    if pat.match(line):
        print(line)
        break
else:
    print("No email")