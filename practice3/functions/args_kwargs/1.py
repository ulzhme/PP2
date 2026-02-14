# 1. Произвольные аргументы (*args) - передаются как кортеж
def list_kids(*kids):
    print("The second child is " + kids[1])
list_kids("Emil", "Tobias", "Linus")