def main():
    student = get_student() 
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    #print(f"{name} from {house}")
    print(f"{student['name']} from {student['house']}") 

def get_student():
    
    student = {} # student dict is created here
    student["name"] = input("Name: ") # we are assigning values to the dict
    student["house"] = input("House: ")
    return {"name": name, "house": house}
    # name = input("Enter the name: ")
    # house = input("Enter the house name: ")
    # return [name, house] # we are returning one tuple now two variables
    # tuples are immutable which means the value cannot be changed.
    # list is muttable but tuples are immutable
    

# we used tuple, which is a collection of values. 

if __name__ == "__main__":
    main()
    
# tuple object does not support item assignment    
# in list you can assign value to the object
# in tuple your can't overwrite the existing value, but in list you can overwrite the existing value. 

# dict is the collection of key and value







