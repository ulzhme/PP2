n = int(input())
db = {}

for i in range(n):
    vvod = input().split()
    komanda = vvod[0]
    klyuch = vvod[1]

    if komanda == "set":
        znachenie = vvod[2]
        db[klyuch] = znachenie
    
    if komanda == "get":
        if klyuch in db:
            print(db[klyuch])
        else:
            print("KE: no key", klyuch, "found in the document")
