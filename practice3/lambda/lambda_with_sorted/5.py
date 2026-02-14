# 5. Сортировка списка чисел по их абсолютному значению
nums = [-15, 10, -5, 20]
sorted_abs = sorted(nums, key=lambda x: abs(x))
print(sorted_abs)