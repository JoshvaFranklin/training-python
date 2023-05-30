import sys
# check for errors
'''
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:        
    print("hello, my name is", sys.argv[1])
'''

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# for arg in sys.argv:
#     print("hello, my name is", arg)    

# for arg in sys.argv[1:]:
#     print("hello, my name is", arg)   

for arg in sys.argv[1:-1]: #using slices to avoid name.py which is in position 0
    print("hello, my name is", arg)    

    
