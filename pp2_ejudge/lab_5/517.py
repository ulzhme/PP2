import re

s = input()

x = re.findall(r'[0-9]{2}+/{1}+[0-9]{2}+/{1}+', s)
print(len(x))