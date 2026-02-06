n = int(input())
slovar = {}

for i in range(1, n + 1):
    slovo = input()
    if slovo not in slovar:
        slovar[slovo] = i

kluchi = sorted(slovar.keys())

for slovo in kluchi:
    print(slovo, slovar[slovo])
