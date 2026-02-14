class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        return self.base_salary + (self.base_salary * self.bonus_percent / 100)

class Developer(Employee):
    def __init__(self, name, base_salary, projects):
        super().__init__(name, base_salary)
        self.projects = projects

    def total_salary(self):
        return self.base_salary + (self.projects * 500)

class Intern(Employee):
    pass

line = input().split()
job_title = line[0]
name = line[1]
salary = int(line[2])

if job_title == "Manager":
    bonus = int(line[3])
    worker = Manager(name, salary, bonus)
elif job_title == "Developer":
    num_projects = int(line[3])
    worker = Developer(name, salary, num_projects)
else:
    worker = Intern(name, salary)

print(f"Name: {worker.name}, Total: {worker.total_salary():.2f}")