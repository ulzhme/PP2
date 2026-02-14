# 2. Класс "Смартфон" (Телефон + Камера)
class Phone:
    def call(self): print("Calling...")

class Camera:
    def take_photo(self): print("Photo taken")

class SmartPhone(Phone, Camera):
    pass