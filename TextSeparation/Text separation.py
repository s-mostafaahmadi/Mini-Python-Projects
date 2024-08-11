import os
import string
import re
os.system("cls")
print("-------------correction of sentences---------------")
list_mojaz=['ä','ö','ü','ß','.','?','!',' ']
for i in string.printable[10:62]:
    list_mojaz.append(i)
# print(list_mojaz) 

# namefile=input("Enter your folder name :(with the format)")

namefile= "INPUT.txt"

file_old = open(f"{namefile}","r",encoding='utf-8')
list_sentence=file_old.readlines()

file_new = open("OUTPUT.txt","w",encoding='utf-8')

for i in list_sentence:
    if(re.search("^[-a-zA-Z]+",i)):
        test=i.strip()
        for j in test:
            if j in list_mojaz:
                file_new.write(j)
        file_new.write("\n")
