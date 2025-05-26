size = int(input("Enter the size of the pattern: "))

value = 1

while value <= size:
    print(' ')
    for i in range(size):
        print('*', end="")
    value += 1 

