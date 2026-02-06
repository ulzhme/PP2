n, l, r = map(int, input().split())
a = list(map(int, input().split()))
l = l - 1
a[l:r] = a[l:r][::-1]

print(*a)
