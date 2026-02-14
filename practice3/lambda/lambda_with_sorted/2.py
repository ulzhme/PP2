# 2. Сортировка строк по их длине
fruits = ["strawberry", "apple", "kiwi", "banana"]
fruits.sort(key=lambda s: len(s))
print(fruits)