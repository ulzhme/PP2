# 3. Сортировка словаря по значениям (цены)
prices = {"apple": 50, "orange": 20, "banana": 40}
sorted_prices = sorted(prices.items(), key=lambda item: item[1])
print(dict(sorted_prices))