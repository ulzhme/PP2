import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

line1 = input().split()
p1 = Point(int(line1[0]), int(line1[1]))
p1.show()

line2 = input().split()
p1.move(int(line2[0]), int(line2[1]))
p1.show()

line3 = input().split()
p2 = Point(int(line3[0]), int(line3[1]))

d = p1.dist(p2)
print(f"{d:.2f}")