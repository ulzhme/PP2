# 3. Взаимодействие методов друг с другом
class Light:
    def __init__(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def status(self):
        return "Light is ON" if self.is_on else "Light is OFF"