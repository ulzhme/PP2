# 1. Использование super() в __init__
class Parent:
  def __init__(self, txt):
    self.message = txt

class Child(Parent):
  def __init__(self, txt, age):
    super().__init__(txt) # Вызывает __init__ родителя
    self.age = age