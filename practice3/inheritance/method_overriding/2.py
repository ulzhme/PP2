# 2. Изменение стандартного поведения (Математика)
class Calculator:
    def calculate(self, x, y):
        return x + y

class Multiplier(Calculator):
    def calculate(self, x, y):
        return x * y