# 4. Цикл по **kwargs для вывода всех данных
def show_profile(**user):
    for key, value in user.items():
        print(f"{key}: {value}")
show_profile(username="coder123", status="active", points=50)