class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa

    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")

data = input().split()
if len(data) >= 2:
    name_input = data[0]
    gpa_input = float(data[1])
    
    student_obj = Student(name_input, gpa_input)
    student_obj.display()