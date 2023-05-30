# Building basic calulator using functions in python

# main function 

def main():
   
    num1 = int(input("Enter the First number: "))

    num2 = int(input("Enter the Second number: "))

# display the result

    print("Addition is: ",add(num1,num2))
    print("Subtraction is: ",sub(num1,num2))
    print("Multiplication is: ",mul(num1,num2))
    print("Divison is: ",div(num1,num2))
    
# functions for operations

def add(n1,n2):
    return n1+n2
    
def sub(n1,n2):
    return n1-n2
    
def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

# calling the main function 

main()


    

