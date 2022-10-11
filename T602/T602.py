"""Light version of a _hINESorical text file editor T602.

Current features:
    1. Create a new text file or celect an e_xINESing one to edit.
    2. Write a line of text and save the line to the file.
    3. Use special commands: >S - SAVE&EXIT, >E - EXIT, >B - BACKSPACE 

To debug:
    - backspace command sometimes creates an extra blank line???
    - location of the text files differs from the current folder of T602.py WHY?

Future features:
    - create classes
        EditFile, PrintScreen
    - revise and upload the final project to github, maybe?
    - is there a way to edit a line insted of deleting it? -> input(defaulValueToEdit=(file_name[-1:]))
    - ...

"""
 
from copy import copy
from datetime import datetime
import os
import sys

# Enter: styletext('text', S.FAIL), by default color = WARNING
import style as S
from style import styletext


# clear console function, use "clearScreen()"
clearScreen = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")


def print_heading(line_no, file_name):        #funkce na vykreslování textu od Pythonu; https://docs.python.org/3/library/string.html#format-specification-mini-language
    """prints heading"""
    clearScreen()
    text1 = f" T602-Lite! You are editing the line '{line_no + 1}' file '{file_name}' "
    text2_temp = " Commands:  >S - SAVE&EXIT, >E - EXIT, >B - BACKSPACE"
    text2 = text2_temp + ((len(text1) - len(text2_temp)) * " ")
    box_side = len(text1) * "═"
    print(styletext(f"╔{box_side}╗\n║{text1}║\n║{text2}║\n╚{box_side}╝", S.OKBLUE))

    
# load file or create a new one
def load_file():
    file_content = []
    default_file_name = "file.txt"
    print(styletext(f"> Enter a file name, {default_file_name} is set by default."))
 
    file_name = input("> ").strip() or default_file_name
 
    if os.path.exists(file_name):
        if os.path.isfile(file_name):
            with open(file_name, "r", encoding="utf-8") as f:
                file_content = f.read().splitlines() # splitlines?
    else:
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                pass
        except OSError:
            print(f"Could not create file {file_name}")
            sys.exit(1) # ?
 
        file_content.append(f':: This {file_name} was created by T602-Lite on {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}.')
    return file_name, file_content
 

def editor():
    """load file, create backup, loop while editing file, use commands to save, exit or backspace"""
    file_content = []
    file_content_backup = []  # copy of file_content for restoration
    input_line = ""  # LINE text variable

    file_name, file_content = load_file()
    file_content_backup = file_content.copy()
 
    while True:
        print_heading(len(file_content), file_name)
        for l in file_content:
            print(l)
    
        input_line = input()
            
        # Standarad behaviour section
        if not input_line.startswith(">"):
            file_content.append(input_line) # file_content.append('\n'+input_line)
 
            with open(file_name, "w", encoding="utf-8") as f:
                f.write("\n".join(file_content))
            continue
 
        # special commands section
        input_line = input_line.upper()
 
        if input_line == ">S":
            print(styletext("> Saved."))
            break
 
        elif input_line == ">E": # proč ne '>E'?
            print(styletext("> Exit, NOT saved."))
            # restore old version from before editting
            if file_content_backup:
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write("\n".join(file_content_backup)) # my version: f.writelines(file_content_backup)
                    f.close()
            else:
                os.remove(file_name)
 
            break
        
        elif input_line.startswith(">B"): # elif input_line[:2].upper() == '>B':
            # counted_backspace = (input_line.upper()).count('B')
            for _ in range((input_line).count("B")):
                try:
                    del file_content[-1] # del file_content[-1:]
                except IndexError:
                    break
        else: # print(styletext(f"> '{input_line}' is not recognised command. Press ENTER to continue without any changes.", S.FAIL))
            print(
                styletext(
                    f"> '{input_line}' is not recognised command. Press ENTER to continue without any changes.",
                    S.FAIL,
                )
            )
            input()
 

def main():
    """the main loop"""
    while 1:
        editor()
        print(styletext("> Press ENTER to terminate T602-Lite, or 'O' to open another file."))
        question = input("> ") # '> '? alt+shift + F ?
        if question.upper() != "O":
            break


if __name__ == '__main__':
    main()
