# 2. Вызов обычного метода родителя
class Animal:
  def eat(self):
    print("Eating...")

class Dog(Animal):
  def eat(self):
    super().eat()
    print("Dog is eating meat")