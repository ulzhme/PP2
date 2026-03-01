# 5 
def squares(a, b):
    for i in range(a, b+1):
        yield i * i

# Test with a for loop
for val in squares(3, 7):
    print(val)