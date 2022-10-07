"""Light version of a historical text file editor T602.

Current features:
    1. Create a new text file or celect an existing one to edit.
    2. Write a line of text and save the line to the file.
    3. Use special commands: >S - SAVE&EXIT, >E - EXIT, >B - BACKSPACE 

To debug:
    - backspace command creates an extra blank line, newline=''???
    - location of the text files differs from the current folder of T602.py WHY?
    - does not count blank lines!

Future features:
    - create classes
        EditFile, PrintScreen
    - codeReview?
    - revise and upload it to github, maybe?
    - is there a way to edit a line insted of deleting it? -> input(defaulValueToEdit=(File[-1:]))
    - ...

"""
from ast import Pass
from datetime import datetime
import os.path

import os

# System call
os.system("")

# Class of different styles; print(Style.YELLOW + "Hello, World!")
class Style():
    #reset style
    RESET = '\033[0m'
    #text styles
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    #others
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# clear console function, use "clearScreen()"
import os
clearScreen = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")

#global variables
File = "file.txt" # File to be edited
FileList = [] #copy of File for restoration
Line = "" #Line text variable
LineNo = 1 #line to be edited

#returns line number
def lineNo():
    try:
        with open(File, 'r', encoding='utf8', newline='') as f:
            lineNo = len(f.readlines()) + 1
            f.close()
        return lineNo
    except:
        return 0

#prints heading
def print_heading():
    clearScreen()
    text1 = (f" T602-Lite! You are editing the line '{lineNo()}' file '{File}' ")
    text2_temp = (" Commands:  >S - SAVE&EXIT, >E - EXIT, >B - BACKSPACE")
    text2 = text2_temp + ((len(text1)-len(text2_temp)) * ' ')
    box_side =  len(text1) * '═'
    print(Style.OKBLUE + f"╔{box_side}╗\n║{text1}║\n║{text2}║\n╚{box_side}╝" + Style.RESET)

#prints the heading and the file content
def print_screen():
    print_heading()
    with open(File, 'r', encoding='utf8', newline='') as f:
        print(f.read())
        f.close()

#returns Continue or Break according to special commands
def special(command):
    if command.upper() == '>S':
        print('> Saved.')
        return "Break"
    elif command.upper() == '>E':
        print(Style.WARNING + '> Exit, NOT saved.' + Style.RESET)
        if FileList == []: os.remove(File)
        else:
            with open(File, 'w', encoding='utf-8', newline='') as f:
                f.writelines(FileList)
                f.close()
        return "Break"
    elif command[:2].upper() == '>B':
        with open(File, 'r', newline='') as f:
            counted = (command.upper()).count('B')
            lines = f.readlines()
            lines = lines[:-counted]
            f.close()
        with open(File, 'w', newline='') as f:
            text = ''.join(lines)
            f.write(text)
            f.close()
        return "Continue"
    else:
        print(Style.FAIL + f"> '{command}' is not recognised command. Press ENTER to continue without any changes." + Style.RESET)
        input()
        return "Continue"
    
#load file or create a new one
def load_file():
    global File
    global FileList
    print(Style.WARNING + "> Enter a file name 'file.txt' is set by default." + Style.RESET)
    file = input('> ')
    if file == '': pass
    else: File = file
    try:
        with open(File, 'x', encoding='utf-8', newline='') as f:
            now = datetime.now()
            f.write(f':: This File was created by T602-Lite on {now.strftime("/%d/%m/%Y %H:%M:%S")}.')
            f.close()
            FileList = []
    except OSError:
        File = 'file.txt'
        with open(File, 'r', encoding='utf-8', newline='') as f:
            FileList = f.readlines()
            f.close()
    except:
        with open(File, 'r', encoding='utf-8', newline='') as f:
            FileList = f.readlines()
            f.close()

def editor():
    print_heading()
    load_file()
    while(1):
        print_screen()
        Line = input()
        if Line != '':
            if Line[0] == '>':
                specialCommand = special(Line)
                if specialCommand == 'Continue': continue
                if specialCommand == 'Break': break
        with open(File, 'a', encoding='utf-8', newline='') as f:
            f.write('\n')
            f.write(Line)
            f.close()

#the main loop
while(1):
    editor()
    print(Style.WARNING + "> Press ENTER to terminate T602-Lite, or 'O' to open another file." + Style.RESET)
    question = input('> ')
    if question.upper() != 'O':
        break

    

    