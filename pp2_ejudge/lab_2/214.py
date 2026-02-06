n = input()
a = list(map(int, input().split()))

chastoe = a[0]
skolko = 0

for x in sorted(a):
    vstrechaetsya = a.count(x)
    if vstrechaetsya > skolko:
        skolko = vstrechaetsya
        chastoe = x

print(chastoe)
