import os
import click
from random import randint


# clear console function
clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")


def addFood(cube_size, cube_space):
    i = 0
    while i <= 3:
        x = randint(1, cube_size) - 1
        y = randint(1, cube_size) - 1
        z = randint(1, cube_size) - 1
        cube_space[z][y][x]
        if cube_space[z][y][x].startswith("E"):
            cube_space[z][y][x] = "F0"
            break
        i += 1

    return cube_space


def printCube(cube_space):
    """prints cube_space in 2D visualisation"""
    next_color = len(cube_space) + 1
    for space in cube_space:
        prev_color = next_color - 1
        print("  " + (getBox("U" + str(prev_color)) + " ") * len(cube_space), end="\n")
        for line in space:
            print(getBox("L" + str(prev_color)), end="")
            for item in line:
                if item[1] != "0":
                    next_color = (int(item[1]) % len(cube_space)) + 1
                print(getBox(item), end=" ")
            print(getBox("R" + str(next_color)), end="\n")
        print(
            "  " + (getBox("D" + str(next_color)) + " ") * len(cube_space), end="\n" * 1
        )


def createCube(cube_size):
    """creates an empty cube_space"""

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


def getBox(atr):
    """Returns state and color according to attribute"""

    # atribute definition
    color = int(atr[1])
    state = atr[0]

    # set and reset color:
    reset_color = "\033[37m"  # reset color
    if color == 0:
        color = "\033[37m"
    else:
        color = color % 5  # + 1
        color = "\033[3" + str(color) + "m"
    # colores = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m'] #red, green, yellow, blue, gray

    # set state/symbol:
    text = ""

    if state == "E":
        text = "\u2610 "  # empty box <= (E)MPTY
    if state == "T":
        text = "\u2612 "  # box with dot <= (T)RACE
    if state == "C":
        text = "\u25a3 "  # full box <= (C)URSOR
    if state == "F":
        text = "\u25a6 "  # mouse <= (F)ood

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
    """sets a cube_space size and do the main loop"""

    clear()
    print("Enter your 3D playground size. (default 5)")
    try:
        cube_size = int(input('> '))
        if cube_size == 1:
            cube_size = 1024
    except:
        cube_size = 1024  # Default size of cube_space.
    clear()

    cube_space = createCube(cube_size)
    # print(cube_space) # Un-comment for to see the structure of cube_space list

    # get initial coordinates
    x = randint(1, cube_size)
    y = randint(1, cube_size)
    z = randint(1, cube_size)

    points = 0

    cube_space[z - 1][y - 1][x - 1] = "C0"
    print(f"Snake 3D - eat them all!\nGet points by eating the food!\n")
    #printCube(cube_space)

    # pre_x, pre_y, pre_z = x, y, z

    # the main loop:
    while True:

        # save future previous coordinates
        pre_x, pre_y, pre_z = x, y, z
        #print("\nChoose direction (wsad)")

        
        # direction = str(click.getchar()).upper()
        # # direction = input("> ").upper().strip()
        # if direction == "W":
        y -= 1
        # elif direction == "S":
        #     y += 1
        # elif direction == "A":
        #     x -= 1
        # elif direction == "D":
        #     x += 1
        # else:
        #     continue

        # justify coordinates:
        # if x > cube_size:
        #     x -= cube_size
        #     z += 1
        # if x == 0:
        #     x += cube_size
        #     z -= 1
        # if y > cube_size:
        #     y -= cube_size
        #     z += 1
        if y == 0:
            y += cube_size
            z -= 1
        # if z > cube_size:
        #     z -= cube_size
        # if z == 0:
        #     z += cube_size

        # collison with tail or food
        pre_position = cube_space[z - 1][y - 1][x - 1]
        if pre_position.startswith("T"):
            pre_position = "T0"
            print(f"Snake 3D - eat them all!\nPOINTS: {points}\n")
            # printCube(cube_space)
            print("Collision!")
            break
        elif pre_position.startswith("F"):
            points += 1

        # record new move
        cube_space[pre_z - 1][pre_y - 1][pre_x - 1] = "T" + str(pre_z)
        cube_space[z - 1][y - 1][x - 1] = "C0"

        # header
        #clear()
        #print(f"Snake 3D - eat them all!\nPOINTS: {points}\n")

        cube_space = addFood(cube_size, cube_space)
        #printCube(cube_space)
    #print(f"Snake 3D - eat them all!\nPOINTS: {points}\n")


if __name__ == "__main__":
    while True:
        main()
        print("OR press (A)again to reset Snake_3D.")
        terminate_question = str(click.getchar()).upper()
        print("")
        if terminate_question.upper() != "A":
            break
