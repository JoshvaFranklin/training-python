# A simple hello world using function

def hello(x="default_name"):
    print("hello,", x)


hello()

name = input("enter your name: ")

hello(name)
    