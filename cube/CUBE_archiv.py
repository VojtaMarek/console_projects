import os
#clear console function, use "clear()"
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#global variables
SPACE_LIST = []

#starting position of the number/cursor
X = 1
Y = 1
Z = 0

#dimensions of the cube
L = 1


def line_to_list(start, length):
    """"adds one line to a list, and changes to start value (True, False)""" #to call this: help(line_to_list)
    position = 0
    new_line = [] #line to be finally added to the global SPACE_LIST
     #finish the line according to the length
    while position < length:
        if start:
            new_line.append("X")
        else:
            new_line.append("O")
        position += 1           #if start is True, make X and add one position
        start = not start
    SPACE_LIST.append(new_line)

def print_list():
    """prints the layer of space according the Z position/coordinate"""
    z_list = SPACE_LIST[Z].copy() 
    for line in z_list:
        for item in line:
            print(item + "  ", end="")
        print("")

def create(dimension):
    """creates the space"""
    start = True
    temp_list = []
    global SPACE_LIST
    for Z_position in range(dimension):
        SPACE_LIST.clear() #!
        for position in range(dimension):
            line_to_list(start, dimension)
            start = not start
        temp_list.append(SPACE_LIST)
        if L%2 == 0:
            start = not start
    SPACE_LIST = temp_list.copy()
    temp_list.clear()

def change_list(x, y, z): #to be upgraded according the last 2D version
    """creates the visual move according the new coordinates"""
    res_x = int(x % L)
    res_y = int(y % L)
    res_z = int(z % L)

    #print("test:", type(res_z)) #un-comment to test the variable type of res_z variable

    SPACE_LIST[res_z][res_y].pop(res_x)
    SPACE_LIST[res_z][res_y].insert((res_x), str(z))

def change_Z_position(): #to be repaired!!!!
    """The problamatic change Z position to get to different dimension"""
    global Z
    if ((Y%L+X%L)%L) > 0: #increase Z positon
        Z += 1
    elif ((Y%L+X%L)%L) < 0: #decrease Z positon
        Z -= 1
    #rest_X = X % L
    #rest_Y = Y % L
    #Z = int((X-rest_X)/L) + int((X-rest_X)/L)

def main():
    """initialization and the main loop"""
    #get the size of cube:
    clear()
    print('Enter a cube side:')
    L = int(input('> '))
    clear()

    X = Y = (L // 2) - 1 #put cursor to the middle on dimesion 0

    create(L) #create the field
    change_list(X, Y, Z)
    print(SPACE_LIST)           #un-comment to see the SPACE_LIST stucture

    #clear()                    #un-comment not to see the SPACE_LIST structure
    print_list()
    
    while True:
        #direction = ""
        print("\nChoose direction (wsad):")
        direction = input('> ')
        if direction == "w": Y -= 1
        elif direction == "s": Y += 1
        elif direction == "a": X -= 1
        elif direction == "d": X += 1
        else: continue
        clear()
        #create(9)
        change_Z_position()
        change_list(X, Y, Z)
        #print("_____________________")
        print_list()

        
if __name__ == '__main__':
    main()





