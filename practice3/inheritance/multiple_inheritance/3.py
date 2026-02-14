# 3. Порядок поиска методов (MRO - Method Resolution Order)
class A:
    def show(self): print("A")

class B:
    def show(self): print("B")

class C(A, B): # Сначала проверит A, потом B
    pass
    