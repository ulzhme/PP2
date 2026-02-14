# 5. Использование self для доступа к другим методам
class MathOps:
    def multiply(self, a, b):
        return a * b
    def square(self, n):
        return self.multiply(n, n) # Вызываем свой же метод через self