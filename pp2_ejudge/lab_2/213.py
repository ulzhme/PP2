x = int(input())

if x < 2:
    print("No")
else:
    isPrime = True
    for i in range(2, x):
        if x % i == 0:
            isPrime = False
            break
    
    if isPrime:
        print("Yes")
    else:
        print("No")
