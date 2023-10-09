class School :
    def open(self) :
        print("First class")
class Class1(School) :
    def start(self) :
        print("Second class")

obj = Class1()
obj.open()
obj.start()