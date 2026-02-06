n = int(input())
kniga = {}

for i in range(n):
    nomer = input()
    if nomer in kniga:
        kniga[nomer] = kniga[nomer] + 1
    else:
        kniga[nomer] = 1

otvet = 0
for klyuch in kniga:
    if kniga[klyuch] == 3:
        otvet = otvet + 1

print(otvet)
