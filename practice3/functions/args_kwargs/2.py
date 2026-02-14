# 2. Использование *args для суммирования любого количества чисел
def add_everything(*numbers):
    return sum(numbers)
print(add_everything(1, 2, 3, 4, 5))