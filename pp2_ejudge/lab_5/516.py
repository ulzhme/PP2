import re

s = input()

x = re.search(r'Name:\s*(.+),\s*Age:\s*(.+)', s)
print(x.group(1), x.group(2))