from datetime import datetime
import sys
import os
import datetime



#modulo datetime
odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 
49, 51, 53, 55, 57, 59 ]

right_this_minute = datetime.today().minute 

if right_this_minute in odds:
    print("Este minuto parece um pouco estranho.")
else:
    print("Nem um minuto estranho.")

#modulo sys
print("==Este é o modulo sys, no qual apresenta a versão do python e sistema op==")
print(sys.version) 

#modulo OS
print("***Este é o modulo OS***")
print(os.getcwd()) 


