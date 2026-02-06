n = input()
spisok = list(map(int, input().split()))

bolshoe = max(spisok)
mesto = spisok.index(bolshoe)

print(mesto + 1)
