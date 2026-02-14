# 3. super() в многоуровневом наследовании
class A:
    def greet(self): print("Hello from A")

class B(A):
    def greet(self): super().greet()