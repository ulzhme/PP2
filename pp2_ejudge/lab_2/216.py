n = input()
a = map(int, input().split())

pamyat = set()

for x in a:
    if x in pamyat:
        print("NO")
    else:
        print("YES")
        pamyat.add(x)
