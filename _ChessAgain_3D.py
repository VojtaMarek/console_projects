#clear console function
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
#clearConsole()


#global variables
List = []

#starting position of the number
X = 1
Y = 1
Z = 0

#dimension of the cube
L = 3

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
    z_list = List[Z].copy() 
    for line in z_list:
        for item in line:
            print(item + "  ", end="")
        print("")

def create__XX(dimension):
    start = True
    for position in range(dimension):
        for z_position in range(dimension):
            line_to_list(start, dimension, z_position)
            start = not start
        start = not start

def create(dimension):
    start = True
    temp_list = []
    global List
    for Z_position in range(dimension):
        List.clear() #!
        for position in range(dimension):
            line_to_list(start, dimension)
            start = not start
        temp_list.append(List)
        if L%2 == 0:
            start = not start
    List = temp_list.copy()
    temp_list.clear()


def change_list(x, y, z): #to be upgraded according the last 2D version
    res_x = int(x % L)
    res_y = int(y % L)
    res_z = int(z % L)

    print("test:", type(res_z))

    List[res_z][res_y].pop(res_x)
    List[res_z][res_y].insert((res_x), str(z))

def change_Z_position(): #to be repaired
    global Z
    if ((Y%L+X%L)%L) > 0: #increase Z positon
        Z += 1
    elif ((Y%L+X%L)%L) < 0: #decrease Z positon
        Z -= 1
    #rest_X = X % L
    #rest_Y = Y % L
    #Z = int((X-rest_X)/L) + int((X-rest_X)/L)


create(L) #dimension of the squered field

change_list(X, Y, Z)
#print(List)

clearConsole()
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
    change_Z_position()
    change_list(X, Y, Z)
    #print("_____________________")
    print_list()

        






