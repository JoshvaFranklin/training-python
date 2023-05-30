def even_or_odd():
    x = e_o() #hiding the operation behind this even or odd function
    # print(f"x was {x}")

def e_o():
           
    try: # using exception to make sure that we get an int for a num and not a string
        num = int(input("Enter a number: "))
        
        if (num % 2 == 0):
            print("It's Even")           
        else:
            print("It's Odd")
        
        return num    
    except TypeError: # this is for checking for any type error
        print("not all arguments converted during string formatting.")  
    except ValueError:  # this is for checking for any value error 
        print("Invalid Literal for integer.")     
    except NameError:   # this is for checking for any name error
        print("Name is not defined.")    
         
                     
even_or_odd()   
   
     


                


        
        