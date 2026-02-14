# 4. Объединение способностей (Миксины)
class SwimMixin:
    def swim(self): print("Swimming...")

class FlyMixin:
    def fly(self): print("Flying...")

class Duck(SwimMixin, FlyMixin):
    pass