n = input()
chisla = map(int, input().split())

otvet = []

for x in chisla:
    kvadrat = x * x
    otvet.append(kvadrat)

print(*otvet)
