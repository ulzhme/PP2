# 2. Счетчик созданных объектов
class Student:
    total_students = 0 # Общий счетчик
    def __init__(self, name):
        self.name = name
        Student.total_students += 1