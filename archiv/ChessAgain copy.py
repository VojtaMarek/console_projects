#clear console function
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
#clearConsole()


#global variables
List = []
X = 4
Y = 4

def line_to_list(start, length):
    position = 0
    new_line = []
    #if start is True, make XXX and add a position
     #finish the line according to the length
    while position < length:
        if start:
            new_line.append("X")
        else:
            new_line.append("O")
        position += 1
        start = not start
    List.append(new_line)

def print_list():
    for line in List:
        for item in line:
            print(item + "  ", end="")
        print("")

def create(dimension):
    start = True
    for position in range(dimension):
        line_to_list(start, dimension)
        start = not start

def change_list(x, y):
    List[y].pop(x)
    List[y].insert(x, ".")

create(9) #dimension of the squered field
print_list()
change_list(X, Y)
#print(List)
print_list()

        






