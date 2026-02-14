# 2. Поиск слов длиннее 4 букв
words = ["dog", "apple", "cat", "banana"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)