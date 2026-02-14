class Base1:
    def __init__(self): self.str1 = "Geek1"

class Base2:
    def __init__(self): self.str2 = "Geek2"

class Final(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)