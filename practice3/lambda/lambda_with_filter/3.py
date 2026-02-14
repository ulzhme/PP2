# 3. Фильтрация только положительных чисел
data = [-5, 3, -1, 10, 0, 7]
positives = list(filter(lambda x: x > 0, data))
print(positives)