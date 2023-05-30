# class --> allow you to define custom container with custom name

class Student:
    pass

def main():
    student = get_student()
    print(f"{student.name} from {Student.house}")

def get_student():
    student = Student() # calling the class as we call a function
    # classes have 
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


    

