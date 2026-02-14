# 5. Извлечение первого символа из слов
words = ["Python", "Lambda", "Map"]
first_letters = list(map(lambda s: s[0], words))
print(first_letters)