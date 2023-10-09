class Employee :
    def __init__(self) :
        self.id = 123
        self.name = "Melvin"
    def display(self) :
        print("Hi")

emp1 = Employee()
print(emp1.id)
emp1.display()