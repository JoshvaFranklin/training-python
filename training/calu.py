# A simple calculator using Class and Fucntions

num1 = int(input("enter the first number: "))

num2 = int(input("enter the second number: "))


class calculator:
    
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        add = self.number1 + self.number2
        print("addition is: ", add)
    def sub(self):
        sub = self.number1 - self.number2
        print("subtraction is: ", sub)
    def mul(self):
        mul = self.number1 * self.number2
        print("multiplication is: ", mul)
    def div(self):
        div = self.number1 / self.number2
        print("divison is: ", div)

r = calculator(num1,num2)
r.add()
r.sub()
r.mul()
r.div()

