class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)  
        self.emp_id = emp_id
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)  
        self.department = department

    def display(self):
        self.display_person()
        self.display_employee()
        print("Department:", self.department)
        print("-" * 20)



m1 = Manager("ASlice", 30, "E123", 50000, "HR")
m2 = Manager("Sarvesh", 18, "E125", 60000000000,"CTO")
m3 = Manager("Ayushi Ghosh", 19, "E124", 70000000000, "CEO")
m4 = Manager("Shaswat Barde", 19, "E126", "15L", "Director")
m1.display()
m2.display()
m3.display()
m4.display()