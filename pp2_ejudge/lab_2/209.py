n = input()
spisok = list(map(int, input().split()))

bolshoe = max(spisok)
malenkoe = min(spisok)

for i in range(len(spisok)):
    if spisok[i] == bolshoe:
        spisok[i] = malenkoe

print(*spisok)
