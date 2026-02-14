# 5. Сочетание стандартного аргумента, *args и **kwargs
def master_func(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Extra positional: {args}")
    print(f"Extra keyword: {kwargs}")
master_func("Alex", 1, 2, city="Almaty", age=20)