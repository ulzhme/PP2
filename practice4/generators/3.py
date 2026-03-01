# 3  Generator for numbers 
# divisible by 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage
for num in divisible_by_3_and_4(50):
    print(num)
