# 2 Generator for even numbers between
#  0 and n (comma-separated)
def even_numbers(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i
n = int(input("Enter a number: "))
print(",".join(str(num) for num in even_numbers(n)))
