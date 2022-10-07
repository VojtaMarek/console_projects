#clear console function
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
#clearConsole()


#global variables
List = []
X = 4
Y = 4
L = 9

def line_to_list(start, length):
    position = 0
    new_line = [] #line to be finally added to the global List
    #if start is True, make X and add a position
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
    List[(y%L)].pop((x%L))
    List[(y%L)].insert((x%L), ".")

create(L) #dimension of the squered field

change_list(X, Y)
#print(List)

#clearConsole()
print_list()

while(1):
    #direction = ""
    direction = input("Direction (wsad) ? ")
    if direction == "w":
        Y -= 1
    elif direction == "s":
        Y += 1
    elif direction == "a":
        X -= 1
    elif direction == "d":
        X += 1
    else:
        continue
    clearConsole()
    #create(9)
    change_list(X, Y)
    #print("_____________________")
    print_list()

        






