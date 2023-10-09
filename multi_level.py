class School :
    def std1(self):
        print("melvin")
class School2(School) :
    def std2(self):
        print("sibin")
class School3(School2) :
    def std3(self):
        print("shebin")
obj1 = School3()


obj1.std1()
obj1.std2()
obj1.std3()