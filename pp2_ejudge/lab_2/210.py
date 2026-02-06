n = input()
spisok = list(map(int, input().split()))

spisok.sort(reverse=True)

print(*spisok)
