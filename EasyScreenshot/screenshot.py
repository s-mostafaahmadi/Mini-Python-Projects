from PIL import ImageGrab
import time
import sys , os
current_time = time.localtime()

year = current_time.tm_year
month = current_time.tm_mon
day = current_time.tm_mday
hour = current_time.tm_hour
minute = current_time.tm_min
second = current_time.tm_sec

print()

listorg=[]
print(os.listdir())
for i in os.listdir():
    try:
        i,Format=i.split(".")
        listorg.append(int(i))
    except:
        continue
sc = ImageGrab.grab()
sc.save(f"{year}{month}{day}_{hour}{minute}{second}.png")

