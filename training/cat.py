'''
print("meow\n" * 3, end="")
# using end ="" to remove the last empty line in the output due to /n
'''

def main():
    number = get_num()
    meow(number)


def get_num():
    while True:
        n = int(input("Enter the number: "))
        if n > 0:
            break
    return n

    
def meow(n):
    for _ in range(n):
        print("meow")    

main()        