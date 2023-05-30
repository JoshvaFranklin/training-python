import cowsay
import sys

if len(sys.argv) == 2:
    #cowsay.cow("hello, " + sys.argv[1])
# can pass only one string in cowsay unlike print function
    cowsay.trex("hello, " + sys.argv[1])
    
    
