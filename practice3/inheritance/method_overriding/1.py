# 1. Простое переопределение метода
class Bird:
    def fly(self):
        print("Most birds can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly, they swim") # Изменяем логику