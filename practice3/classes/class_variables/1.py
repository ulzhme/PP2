# 1. Переменная класса (Class Variable)
class Dog:
    species = "Canis familiaris" # Общая для всех собак
    def __init__(self, name):
        self.name = name # Индивидуальная для каждой собаки