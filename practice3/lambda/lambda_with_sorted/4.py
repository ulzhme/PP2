# 4. Сортировка с игнорированием регистра
letters = ["c", "A", "b", "D"]
sorted_letters = sorted(letters, key=lambda x: x.lower())
print(sorted_letters)