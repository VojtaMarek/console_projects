import os


# clear console function
clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")


def printCube(cube):
    """prints cube in 2D visualisation"""
    next_color = len(cube) + 1
    for space in cube:
        prev_color = next_color - 1
        print("  " + (getBox("U" + str(prev_color)) + " ") * len(cube), end="\n")
        for line in space:
            print(getBox("L" + str(prev_color)), end="")
            for item in line:
                if item[1] != '0':
                    next_color = (int(item[1]) % len(cube)) + 1
                print(getBox(item), end=" ")
            print(getBox("R" + str(next_color)), end="\n")
        print("  " + (getBox("D" + str(next_color)) + " ") * len(cube), end="\n" * 2)


def createCube(cube_size):
    """creates the space of cube"""
    cube_space = []
    square_space = []
    square_space_temp = []
    line_space = []
    line_space_temp = []

    for z in range(cube_size):  # z axe dimension
        for y in range(cube_size):  # y axe dimension
            for x in range(cube_size):  # x axe dimension
                line_space.append("E" + str(z + 1))
            line_space_temp = line_space.copy()
            line_space.clear()
            square_space.append(line_space_temp)
        square_space_temp = square_space.copy()
        square_space.clear()
        cube_space.append(square_space_temp)
    return cube_space


def getBox(atr): # 'atr' is composed by letter and number, corresponding to state and color, respectively.
    """Returns state and color according to attribute"""

    # set and reset color:
    color = int(atr[1])
    reset_color = "\033[0m"  # reset color
    if color == 0:
        pass  # reset color
    else:
        color = (color % 5)# + 1
    color = "\033[3" + str(color) + "m"
    # colores = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m'] #red, green, yellow, blue, purple

    # set state/symbol:
    state = atr[0]
    text = ""

    if state == "E":
        text = "\u2610 "  # empty box <= (E)MPTY
    if state == "T":
        text = "\u2612 "  # box with dot <= (T)RACE
    if state == "C":
        text = "\u25a3 "  # full box <= (C)URSOR

    if state == "U":
        text = "\u25b4 "  # indication (U)P to another space
    if state == "L":
        text = "\u25c2 "  # indication (L)EFT to another space
    if state == "R":
        text = "\u25b8 "  # indication (R)IGHT to another space
    if state == "D":
        text = "\u25be "  # indication (D)OWN to another space

    return f"{color}{text}{reset_color}"


def main():
    """sets a cube size and do the main loop"""

    print("Enter a cube size:")
    try:
        cube_size = int(input("> "))
    except:
        cube_size = 5  # Default size of cube.
    clear()

    cube = createCube(cube_size)
    # print(cube) # Un-comment for to see the structure of cube list

    # get initial coordinates
    z = 1
    x = y = (cube_size // 2) + 1

    cube[z - 1][y - 1][x - 1] = "C0"
    printCube(cube)

    # pre_x, pre_y, pre_z = x, y, z

    # the main loop:
    while True:
        # save future previous coordinates
        pre_x, pre_y, pre_z = x, y, z

        print("\nChoose direction (wsad):")
        direction = input("> ").upper().strip()
        if direction == "W":
            y -= 1
        elif direction == "S":
            y += 1
        elif direction == "A":
            x -= 1
        elif direction == "D":
            x += 1
        else:
            continue
        clear()

        # justify coordinates:
        if x > cube_size:
            x -= cube_size
            z += 1
        if x == 0:
            x += cube_size
            z -= 1
        if y > cube_size:
            y -= cube_size
            z += 1
        if y == 0:
            y += cube_size
            z -= 1
        if z > cube_size:
            z -= cube_size
        if z == 0:
            z += cube_size

        # check for collison and terminat in case:
        if cube[z - 1][y - 1][x - 1].startswith("T"):
            cube[z - 1][y - 1][x - 1] = "T0"
            printCube(cube)
            print("Collision!")
            input()
            break

        # record new move
        cube[pre_z - 1][pre_y - 1][pre_x - 1] = "T" + str(pre_z)
        cube[z - 1][y - 1][x - 1] = "C0"
        printCube(cube)


if __name__ == "__main__":
    while True:
        main()
        print("Press ENTER to terminate or enter 'A' to continue.")
        terminate_question = input("> ")
        if terminate_question.upper() != "A":
            break
