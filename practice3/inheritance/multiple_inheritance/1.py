# 1. Базовый пример множественного наследования
class Engine:
    def start_engine(self): print("Engine started")

class Wheels:
    def rotate(self): print("Wheels rotating")

class Car(Engine, Wheels):
    pass