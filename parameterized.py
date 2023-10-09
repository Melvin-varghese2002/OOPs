class Student :
    def __init__(self,name,address):
        self.name1 = name
        self.address1 = address
    def open(self) :
        print(self.name1)
obj = Student("Melvin","Tiruvalla")
obj.open()
obj.name1 = "Sibin"
obj.open()
obj1 = Student("Shebin","Pathanamthitta")
print(obj1.name1)
print(obj1.address1)