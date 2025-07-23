import time

hour = time.localtime().tm_hour
min = time.localtime().tm_min
sec = time.localtime().tm_sec

current_time = hour + (min/60) + (sec/3600)

print("TIME:", hour, ":", min, ":", sec)

if(current_time >= 5 and current_time <= 12):
    print("Good Morning!")
elif(current_time > 12 and current_time <= 16):
    print("Good Afternoon!")
elif(current_time > 16 and current_time <= 24):
    print("Good Evening!")
else:
    print("Good Night!")