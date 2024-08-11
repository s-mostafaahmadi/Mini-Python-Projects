import os
import win32com.client
from pathlib import Path


def scan_dir():
    os.chdir(r"C:\Users")
    list_dir=[]
    for i in os.listdir():
        if Path(r"C:\Users\\"+i).is_dir():
            try:
                os.chdir(r"C:\Users\{0}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(i))
                list_dir.append(os.getcwd()+"\\")
            except:
                continue

    return list_dir



def create_shortcut(target_path, shortcut_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    shortcut.save()

def main(target_file_path):
    list_dir = scan_dir()
