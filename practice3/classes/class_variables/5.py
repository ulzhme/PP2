# 5. Переопределение переменной класса в объекте
class Bird:
    can_fly = True

penguin = Bird()
penguin.can_fly = False # Изменили только для пингвина