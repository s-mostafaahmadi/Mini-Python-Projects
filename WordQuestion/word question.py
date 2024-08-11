from random import randint
import sys , re
# #open and read the file after the appending:

def append_without_repeated(words):
    f=open("saved.txt","a+")
    f.seek(0)
    file_words=f.read()
    # print(file_words)
    list_new=[]
    if "," in words:
        words=words.split(",")
        for i in words:
            if i not in file_words:
                f.write(i + ',')
    else:
        if words in file_words:
            return file_words
        else:
            f.write(words + ',')

    f.seek(0)
    a=f.read()
    f.close()
    return a


words=input("Enter your words to form (word:answare) and put a comma between this word and another word:")


a=re.search("^([a-zA-Z]* *[a-zA-Z]*)*:([a-zA-Z]* *[a-zA-Z]*)*",words)
if not a and words!="":
    print("The format of your input words is wrong. Please enter in the format that was mentioned")
    sys.exit()

words=append_without_repeated(words)

List_word=words.split(",")
List_word.remove('')
Quiz=[]
Answare=[]
# if not ':' in i:

for i in List_word:
    q,a=i.split(":")
    Quiz.append(q)
    Answare.append(a)

number_random=randint(0,len(List_word)-1)
true=0
rep=0
count_quiz=1
t=True
while t:
    user_ans=input(f"What does {Quiz[number_random]} mean ?")
    if user_ans=="exit":
        if true!=0:
            rabete=count_quiz/true
            score=20/rabete
        else:
            score=0
        print(f"Number of questions : {count_quiz}\nNumber of True : {true}\nScore : {score}")
        sys.exit()


    elif user_ans == Answare[number_random]:
        if rep==0:
            true+=1
        print("True")
        number_random=randint(0,len(List_word)-1)
        count_quiz+=1
        rep=0

    else:
        print("False")
        rep+=1

