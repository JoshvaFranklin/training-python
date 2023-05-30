'''
while True:
    try:
        x = int(input("What's x? "))
    #print(f"x is {x}") #ValueError
    except ValueError:
       print("X is not a Integer")    
    else: 
        print(f"x is {x}") #NameError

# indentation is very improtant 
'''
'''
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")
    #else:
    #    break

print(f"x is {x}")

def main():
    x = get_int()
    print(f"x is {x}")



def get_int():
    while True:
        try:
            x = int(input("Enter the number: "))
            return x
           #break
        except ValueError:
            pass
        #print("Enter an integer")
         #else:
         #   return x      

main()
'''

def main():
    x = get_int("What's the code: ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
           # print("Enter an integer")
            pass
main()



