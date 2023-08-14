import datetime
import time


#Modulo data atual

right_this_data = datetime.date.today()
print(right_this_data)
print(datetime.date.today())

#Modulo hora atual

print("Hora atual...",time.strftime("%H:%M:%S"))
print(time.strftime("%A %p"))