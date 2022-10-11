import os
#clear console function, use "clear()"
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#global variables
List = []   #pojmenovat jinak

#starting position of the number
X = 1
Y = 1
Z = 0

#dimensions of the cube
L = 1

""""adds one line to a list, and changes to start value (True, False)""" #dát dovnitř do funkce, dot.string - help(line_to_list)
def line_to_list(start, length):
    position = 0
    new_line = [] #line to be finally added to the global List
     #finish the line according to the length
    while position < length:
        if start:
            new_line.append("X")
        else:
            new_line.append("O")
        position += 1           #if start is True, make X and add one position
        start = not start
    List.append(new_line)

"""prints the layer of space according the Z position/coordinate"""
def print_list():
    z_list = List[Z].copy() 
    for line in z_list:
        for item in line:
            print(item + "  ", end="")
        print("")


"""creates the space"""
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

"""creates the visual move according the new coordinates"""
def change_list(x, y, z): #to be upgraded according the last 2D version
    res_x = int(x % L)
    res_y = int(y % L)
    res_z = int(z % L)

    #print("test:", type(res_z)) #un-comment to test the variable type of res_z variable

    List[res_z][res_y].pop(res_x)
    List[res_z][res_y].insert((res_x), str(z))

"""The problamatic change Z position to get to different dimension"""
def change_Z_position(): #to be repaired!!!!
    global Z
    if ((Y%L+X%L)%L) > 0: #increase Z positon
        Z += 1
    elif ((Y%L+X%L)%L) < 0: #decrease Z positon
        Z -= 1
    #rest_X = X % L
    #rest_Y = Y % L
    #Z = int((X-rest_X)/L) + int((X-rest_X)/L)

"""initialization below"""
#get the size of cube:
clear()
print('Enter a cube side:')
L = int(input('> '))
clear()

#put cursor to the middle on dimesion 0
X = Y = (L // 2) - 1

create(L) #create the field
change_list(X, Y, Z)
print(List)  #un-comment to see the list stucture

clear()
print_list()


"""The main loop""" #__main__ funkce
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

        






