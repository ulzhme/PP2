# 1 Generator for squares up to N
def generate_squares(N):
    for i in range(1, N+1):
        yield i * i
        
for square in generate_squares(5):
    print(square)

