class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Pair(new_a, new_b)

data = list(map(int, input().split()))
if len(data) == 4:
    p1 = Pair(data[0], data[1])
    p2 = Pair(data[2], data[3])
    
    res = p1.add(p2)
    print(f"Result: {res.a} {res.b}")