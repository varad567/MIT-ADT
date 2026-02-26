class Student:
    
    def accept_details(self):
        self.name = input("Enter student name: ")
        self.roll_no = int(input("Enter roll number: "))
        self.phys = float(input("Enter physics marks: "))
        self.chem = float(input("Enter chemistry marks: "))
        self.maths = float(input("Enter maths marks: "))
    

    def calculate_total(self):
        return self.phys + self.chem + self.maths   
        
    
    def calculate_average(self):
        total = self.calculate_total()
        average = total / 3
        return average
    
    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Physics Marks:", self.phys)
        print("Chemistry Marks:", self.chem)
        print("Maths Marks:", self.maths)
        print("Total Marks:", self.calculate_total())
        print("Average Marks:", self.calculate_average())



student1 = Student()

student1.accept_details()
student1.display() 