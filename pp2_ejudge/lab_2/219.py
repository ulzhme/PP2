n = int(input())
d = {}

for i in range(n):
    slovo, chislo = input().split()
    chislo = int(chislo)
    
    if slovo in d:
        d[slovo] = d[slovo] + chislo
    else:
        d[slovo] = chislo

for s in sorted(d):
    print(s, d[s])
