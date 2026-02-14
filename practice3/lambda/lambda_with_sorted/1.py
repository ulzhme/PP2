# 1. Сортировка списка кортежей по второму элементу (возраст)
users = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
sorted_users = sorted(users, key=lambda user: user[1])
print(sorted_users)