import os 
from os import path
from random import randint
import subprocess
import re
import shutil

def fileorfolder(filename):
    if path.isdir(filename) == True:
        return True
    else:
        return False

def sorte(esf):
    folderlist=[]
    filelist=[]
    for i in esf:
        if path.isdir(i) == True:
            folderlist.append(i)
        else:
            filelist.append(i)
    return filelist+folderlist

#-------------------------------------------------------------------------------


os.chdir(r"c:\Users\mOsTaFa\Desktop")
FirstAddress=r"c:\Users\mOsTaFa\Desktop"

global stack
stack=sorte(os.listdir())

Forbidden_list=['preparing.py','shoooooooooooooood.py']

def delete(stack):
    for i in range(len(stack)):
        if stack[0] not in Forbidden_list:
            # print(stack[0])
            try:
                shutil.rmtree(stack[0])
            except:
                ...
        stack.remove(stack[0])

def create(address=os.getcwd()):
    for i in range(10):
        newpath=f"{address}\\{i}"
        os.mkdir(newpath)
        os.chdir(newpath)
        shutil.make_archive(f"soli{i}",'zip')
        f = open(f"myfirstfile{i}.txt", "x")
        f.close()
    

    # os.mkdir("a")
    # os.mkdir("d")

def getformat(Target):
    try:
        return Target.rsplit(".",1)[-1]
    except:
        ...

def delformat(Target):
    try:
        return Target.rsplit(".",1)[0]
    except:
        ...

def Exited():
    backaddress=os.getcwd().rsplit("\\",1)[0]+"\\"
    print("back to address : ",backaddress)
    os.chdir(backaddress)

delete(stack)
create()
