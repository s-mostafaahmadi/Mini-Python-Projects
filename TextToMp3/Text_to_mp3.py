from gtts import gTTS
import os
from datetime import datetime

def text_to_speech(input_text, output_file):
    # زبان مورد نظر (آلمانی)
    language = 'en'

    # ایجاد یک شی gTTS
    tts = gTTS(text=input_text, lang=language, slow=False)

    # ذخیره فایل صوتی
    os.system(f"mkdir SavedFiles\\{NewName}")
    tts.save(f"SavedFiles\\{NewName}\\{output_file}")
    os.system(f"copy Input.txt SavedFiles\\{NewName}\\{NewName}.txt")
    # پخش فایل صوتی (اختیاری)
    # os.system("start " + output_file)  # برای ویندوز
    # os.system("xdg-open " + output_file)  # برای لینوکس
    # os.system("open " + output_file)  # برای مک

if __name__ == "__main__":
    # متن مورد نظر
    path = os.getcwd()
    file_text = open(f"{path}\\Input.txt", "+r")
    text = file_text.read()
    # text = "Ich möchte einen Artikel."
    NewName =str(datetime.now()).replace(" ","").replace("-","").replace(":","").replace(".","")[0:-6]
    # نام فایل صوتی خروجی
    output_file_name = f"{NewName}.mp3"

    #write a 
    # تبدیل متن به فایل صوتی
    text_to_speech(text, output_file_name)
