import os
from subprocess import check_output
from cryptography.fernet import Fernet

desired_format="txt"

key_file = open("key_Files.txt","rb")
key = key_file.read()
# create class with key
key2 = Fernet(key)
#get files list
fille = check_output(f"D: && dir /S /B *{desired_format}.kilacker",shell=True).decode().split()

key_file.close()

for fileasli in fille:

    name,formatfile,trash=fileasli.split('.',2)
    correct_name=name+'.'+formatfile
    dirlist = open(fileasli,"rb")#rb = ready binary
    token = dirlist.read()
    correct_txt = key2.decrypt(token)
    new_file = open(correct_name,"wb")
    new_file.write(correct_txt)
    new_file.close()
    dirlist.close()
    os.remove(fileasli)

os.remove("key_Files.txt")

# print(fileasli)