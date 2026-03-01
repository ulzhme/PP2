# 4 Generator called squares 
# to yield squares from (a) to (b)
def squares(a, b):
    for i in range(a, b+1):
        yield i * i

for val in squares(3, 7):
    print(val)
