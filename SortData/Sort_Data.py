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

Forbidden_list=['ini','package','مدارک','deutsch']

def main(stack):
    print(stack)
    for i in range(len(stack)):
        Target = stack[0]
        # print(Target)
        stack.remove(stack[0])
        leen=len(stack)

        if Target == 'back':
            Exited()

        elif fileorfolder(Target)==False and getformat(Target) not in Forbidden_list and Target not in Forbidden_list:
            print(Target, " is a file .")
            # print(getformat(Target), " is format this file .")
            # try:
            create_address_mkdir = FirstAddress+f"\\{getformat(Target)}" 
            source = os.getcwd()+"\\"+Target
            # print("address file :",source)
            if path.exists(create_address_mkdir)==False:
                os.mkdir(create_address_mkdir)
                print(f"Folder {getformat(Target)} was created with ", create_address_mkdir, " address")
            try:
                shutil.move(source,create_address_mkdir)
                print(Target , "moved")
                # print("preparing: ",source.rsplit("\\",1)[0]+"\\")
                # shutil.rmtree(source.rsplit("\\",1)[0]+"\\")
            except shutil.Error:
                new_name=f'{delformat(Target)}({randint(0,100)}).{getformat(Target)}'
                os.rename(Target,new_name)
                source2=os.getcwd()+"\\"+new_name
                shutil.move(source2,create_address_mkdir)

            # except:
            #     ...


        elif fileorfolder(Target)==True:
            print(Target, " is a folder .")
            os.chdir(r"{0}\\{1}".format(os.getcwd(),Target))
            # print("open :",os.getcwd())
            stack = os.listdir()+['back']+stack
            main(stack)
            
                
        if(leen==0):
            exit()


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
    sd=os.getcwd().rsplit("\\",1)[1]
    print("back to address : ",backaddress)
    os.chdir(backaddress)
    shutil.rmtree(sd)

main(stack)