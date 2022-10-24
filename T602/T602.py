"""Light version of a hisorical text file editor T602.

    1. Create a new text file or scelect an existing one to edit.
    2. Write a line of text and save the line to the file.
    3. Use special commands: >S - SAVE&EXIT, >E - EXIT, >B - BACKSPACE 
"""

from copy import copy
from datetime import datetime
import os
import sys
from turtle import heading

# Enter: styletext('text', S.FAIL), by default color = WARNING
import style as S
from style import styletext


# clear console function, use "clearScreen()"
clearScreen = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")


def print_heading(line_no=-1, file_name="None"):
    """prints heading"""
    clearScreen()
    text1 = f" T602-Lite! You are editing the line '{line_no + 1}' file '{file_name}' "
    text2_temp = " Commands:  >S - SAVE&EXIT, >E - EXIT, >B - BACKSPACE"
    text2 = text2_temp + ((len(text1) - len(text2_temp)) * " ")
    box_side = len(text1) * "═"
    print(styletext(f"╔{box_side}╗\n║{text1}║\n║{text2}║\n╚{box_side}╝", S.OKBLUE))


def load_file():
    """load or create a new file"""
    file_content = []
    default_file_name = "file.txt"
    print(styletext(f"> Enter a file name, {default_file_name} is set by default."))

    file_name = input("> ").strip() or default_file_name

    if os.path.exists(file_name):
        if not os.path.isfile(file_name):
            print(f"Error - {file_name} is not a file")
            sys.exit(1)

        with open(file_name, "r", encoding="utf-8") as f:
            file_content = f.read().splitlines()
    else:
        file_content.append(
            f':: This {file_name} was created by T602-Lite on {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}.'
        )

    return file_name, file_content


def editor():
    """load file, create backup, loop while editing file, use commands to save, exit or backspace"""
    file_content = []
    input_line = ""

    print_heading()
    file_name, file_content = load_file()

    while True:
        print_heading(len(file_content), file_name)
        for l in file_content:
            print(l)

        input_line = input()

        # standarad behaviour section
        if not input_line.startswith(">"):
            file_content.append(input_line)
            continue

        # special commands section
        input_line = input_line.upper().strip()

        if input_line == ">S":
            with open(file_name, "w", encoding="utf-8") as f:
                f.write("\n".join(file_content))
            print(styletext("> Saved."))
            break

        elif input_line == ">E":
            print(styletext("> Exit, NOT saved."))
            break

        elif input_line.startswith(">B"):
            # counted_backspace = (input_line.upper()).count('B')
            for _ in range((input_line).count("B")):
                try:
                    del file_content[-1]
                except IndexError:
                    break
        else:
            print(
                styletext(
                    f"> '{input_line}' is not recognised command. Press ENTER to continue without any changes.",
                    S.FAIL,
                )
            )
            input()


def main():
    while 1:
        editor()
        print(
            styletext(
                "> Press ENTER to terminate T602-Lite, or 'O' to open another file."
            )
        )
        question = input("> ")
        if question.upper() != "O":
            break


if __name__ == "__main__":
    main()
