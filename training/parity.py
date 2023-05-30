x = int(input("Enter a number: "))

# normal remainder method
'''


if x % 2 == 0 : 
    print("Even")
else:
    print("Odd")
'''

# using function method
        
def is_even(n):
    if n%2==0:
        return True
    else:
        return False

def even_or_odd(x):
    if is_even(x):
        print("Even")
    else:
        print("Odd")    
           
    
even_or_odd(x)
