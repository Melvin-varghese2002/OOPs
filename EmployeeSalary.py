class Employee :
    def __init__(self,name,hourly_rate,hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def salary_calculation (self):
        salary = self.hourly_rate * self.hours_worked
        print("Overall salary of",self.name,"is",salary)

employee1 = Employee("Melvin",50,9)
employee2 = Employee("Sibin",45,9)

employee1.salary_calculation()
employee2.salary_calculation()