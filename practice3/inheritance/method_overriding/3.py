# 3. Переопределение метода __str__ для вывода
class Car:
    def __str__(self):
        return "This is a generic car"

class RaceCar(Car):
    def __str__(self):
        return "This is a fast race car!"