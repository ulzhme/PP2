# 4. Передача списка в качестве аргумента
def my_food(food_list):
    for x in food_list:
        print("Eating: " + x)
fruits = ["apple", "banana", "cherry"]
my_food(fruits)