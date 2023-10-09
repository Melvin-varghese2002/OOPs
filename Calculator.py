class calculation1 :
    def add(self,a,b) :
        return a + b
class calculation2 :
    def sub(self,a,b) :
        return a - b
class calculation3 :
    def mul(self,a,b) :
        return a * b
class calculator(calculation1,calculation2,calculation3) :
    def div(self,a,b) :
        return a / b
d = calculator
print(d.add(10,20,30))
print(d.sub(10,20,40))
print(d.mul(10,20,33))
print(d.div(10,20,21))