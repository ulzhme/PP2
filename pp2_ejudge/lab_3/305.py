class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

try:
    n = int(input())
    
    my_Usquare = Square(n)
    print(my_Usquare.area())
except EOFError:
    pass