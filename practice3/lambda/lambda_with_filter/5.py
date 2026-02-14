# 5. Удаление пустых строк из списка
strings = ["hello", "", "world", " ", "python"]
clean = list(filter(lambda s: s.strip() != "", strings))
print(clean)