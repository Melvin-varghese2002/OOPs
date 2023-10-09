from abc import ABC
class calculator(ABC):
    def add1(self):
        print("Addition")
class calculator1(calculator):
    def sub(self):
        print("Sub")
class calculator2(calculator):
    def multi(self):
        print("multi")
c=calculator2
c.add1()
d=calculator1
d.add1()
