import sys

'''Command line arguments are those values that are passed during calling of program along with the calling statement.
Thus, the first element of the array sys.argv() is the name of the program itself.
sys.argv() is an array for command line arguments in Python. To employ this module named “sys” is used.
sys.argv is similar to an array and the values are also retrieved like Python array.''' 

print("This is the program path", sys.argv[0]) # 'The 0' in sys.argv['0'] is the location of the program name. the program name is always stored in location 0. And the sys module is a array like python's array.

print("the arguments length is", len(sys.argv)) # len function can be used alongside (sys.argv). Thus len(sys.argv) gives the length of '5'

print("the arugements are:", str(sys.argv)) # this str(sys.argv) prints all the input argument passed along with the program name

