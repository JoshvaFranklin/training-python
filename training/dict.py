'''
students = {"Hermione":"Gryffindor",
             "Harry":"Gryffindor",
              "Ron":"Gryffindor",
              "Draco":"Slytherin"}


for student in students:
    print(student, students[student], sep=", ")

'''


'''
student = { 
       "name":"Joshva",
       "age":23,
       "degree":"Btech CSE"
       }

print(student["name"])

# this is ordinary dict and not a nest dict. so we have to retrive data from the dict like this way
'''

# building separate dictionary for each students
# nested dict

students = [
   {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
   {"name": "Harry", "house": "Gryffindor","patronus": "Stag"},
   {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
   {"name": "Draco", "house":"Slytherin", "patronus": "None"}
]

# we stored a dict inside list ;-;

# to retrive data from the dict we use loops now

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")







