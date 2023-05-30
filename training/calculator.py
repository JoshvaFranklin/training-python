def main():

    # functions to get input
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))

    # functions to display result
    print("Addition is: ",add(num1,num2))
    print("Subtraction is: ",sub(num1,num2))
    print("Multiplication is: ",mul(num1,num2))
    
# main calculations are done in below functions

def add(n1,n2):
    return n1+n2

def sub(n1,n2):    
    return n1-n2

def mul(n1,n2):
    return n1*n2 

# calling main function    
main()    
