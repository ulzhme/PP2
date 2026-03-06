import re

ss = input()
x = re.split(r'\s', ss)
cnt = 0
for i in x:
    if len(i) == 3:
        cnt+=1
print(cnt)