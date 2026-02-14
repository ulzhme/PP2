# 4. Поиск строк, начинающихся на 'A'
names = ["Alice", "Bob", "Anna", "Charlie"]
a_names = list(filter(lambda n: n.startswith("A"), names))
print(a_names)