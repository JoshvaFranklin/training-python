def main():
    print_square(3)

def print_square(size):
    # For reach row in square
    for i in range(size):
        print_row(size)
         
def print_row(width):
    print("#" * width)


main()


'''  
For each brick in row
for j in range(size):
Print brick
print("#", end="")
print()
'''
