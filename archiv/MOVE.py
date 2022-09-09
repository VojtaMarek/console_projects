#clear console function
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()


#global variables
list = []



def line_to_list(start, length):
    position = 0
    new_line = []
    #if start is True, make XXX and add a position
    #finish the line according to the length
    while position < length:
        if start:
            new_line.append(":")
        else:
            new_line.append(":")
        position += 1
        start = not start
    list.append(new_line)

def print_list():
    for line in list:
        for item in line:
            print(item + "  ", end="")
        print("")

def create(dimension):
    start = True
    for position in range(dimension):
        line_to_list(start, dimension)
        start = not start

create(8)
#print(list)
print_list()

def change_a_line(x):
    line[0].input()

x = str(input("x: "))
change_a_line(x)




