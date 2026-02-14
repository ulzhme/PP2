# 4. Добавление новых свойств через super()
class Employee(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year