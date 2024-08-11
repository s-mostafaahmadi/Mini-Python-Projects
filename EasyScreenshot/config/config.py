import os
import subprocess
from add_to_startup import main
from pathlib import Path
import win32com.client

main_dir = os.getcwd().rsplit('\\',1)[0]+"\\"


os.chdir(main_dir)

try :
    os.mkdir("Stored")
except:
    ...

path = f"{main_dir}Stored\\"


file = open(f"{main_dir}Screenshot.ahk",'w+')

file.write(f"F8::RUN \"{main_dir}Screenshot.exe\"")

file.close()

os.chdir(path)

target_file_path = f"{main_dir}\Screenshot.ahk"


main(target_file_path)

os.chdir(path)

os.system(target_file_path)
