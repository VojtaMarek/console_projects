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
from ast import Pass
from copy import copy
from datetime import datetime
from fileinput import filename #není nutno importovat from .. (klidně celé knihovny)
import os

#Enter: styletext('text', S.FAIL), by default color = WARNING
import style as S
from style import styletext

# System call
os.system("") #?

# clear console function, use "clearScreen()"
clearScreen = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")


def print_heading(line_no, file = 'None'):        #funkce na vykreslování textu od Pythonu; https://docs.python.org/3/library/string.html#format-specification-mini-language
    """prints heading"""
    clearScreen()
    text1 = (f" T602-Lite! You are editing the line '{line_no + 1}' file '{file}' ")
    text2_temp = (" Commands:  >S - SAVE&EXIT, >E - EXIT, >B - BACKSPACE")
    text2 = text2_temp + ((len(text1)-len(text2_temp)) * ' ')
    box_side =  len(text1) * '═'
    print(styletext(f"╔{box_side}╗\n║{text1}║\n║{text2}║\n╚{box_side}╝", S.OKBLUE))

def print_screen(file_name):
    """prints the heading and the file content"""
    with open(file_name, 'r', encoding='utf8') as f:
        print(f.read())
        f.close()
    
def load_file(file_name, file_content):
    """load file or create a new one"""
    print(styletext(f"> Enter a file name, {file_name} is set by default."))
    imput_name = input('> ')
    file_name_backup = file_name
    if imput_name != '': file_name = imput_name
    try:
        with open(file_name, 'x', encoding='utf-8') as f:
            now = datetime.now()
            file_content.append(f':: This {file_name} was created by T602-Lite on {now.strftime("%d/%m/%Y %H:%M:%S")}.')
    except OSError:
        file_name = file_name_backup
        with open(file_name, 'r', encoding='utf-8') as f:
            file_content = f.readlines()
            f.close()
    except:
        with open(file_name, 'r', encoding='utf-8') as f:
            file_content = f.readlines()
            f.close()
    return file_content

def editor():
    """load file, create backup, loop while editing file, use commands to save, exit or backspace"""
    file_name = "file.txt" # change for diffreent default file name
    file_content = []
    file_content_backup = [] #copy of file_content for restoration
    input_line = "" #LINE text variable

    file_content = load_file(file_name, file_content)
    file_content_backup = file_content.copy()
    print_heading(len(file_content), file_name)
    
    while(1):
        print_heading(len(file_content), file_name)
        if file_content != []: print_screen(file_name)
        input_line = input()
        if input_line != '' and input_line[0] == '>':
            
            #special commands section
            if input_line.upper() == '>S':
                print(styletext('> Saved.'))
                break
            elif input_line.upper() == '>E':
                print(styletext('> Exit, NOT saved.'))
                #restore old version from before editting
                if file_content_backup == []:
                    os.remove(file_name)
                else:
                    with open(file_name, 'w', encoding='utf-8') as f:
                        f.writelines(file_content_backup)
                        f.close()
                break
            elif input_line[:2].upper() == '>B':
                counted_backspace = (input_line.upper()).count('B')
                del file_content[-counted_backspace:]
            else:
                print(styletext(f"> '{input_line}' is not recognised command. Press ENTER to continue without any changes.", S.FAIL))
                input()
                continue
        else: #executed normally
            file_content.append('\n'+input_line)       
        if file_content == []:
            os.remove(file_name)
            break
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(file_content)
            #f.writelines("\n")
            f.close()
        #if file_content == file_content_backup: break #break after saving old version, not on line 118

def main():
    """the main loop"""
    while(1):
        editor()
        print(styletext("> Press ENTER to terminate T602-Lite, or 'O' to open another file."))
        question = input('> ')
        if question.upper() != 'O':
            break


if __name__ == '__main__':
    main()

    