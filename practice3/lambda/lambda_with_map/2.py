# 2. Перевод списка строк в верхний регистр
fruits = ["apple", "banana", "cherry"]
caps = list(map(lambda s: s.upper(), fruits))
print(caps)