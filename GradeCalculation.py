class Students :
    def __init__(self,name,marks) :
        self.name = name
        self.marks = marks
    def grade(self) :
        if self.marks > 50 and self.marks <= 100 :
            print(self.name,"is eligible to write the exam")
        elif self.marks < 50 and self.marks > 0 :
            print(self.name, "is not eligible to write the exam")
        else :
            print("invalid value")
student1 = Students(input("Enter the name :"),int(input("Enter the marks :")))
student2 = Students(input("Enter the name :"),int(input("Enter the marks :")))

student1.grade()
student2.grade()