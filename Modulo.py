#Modulo em python

#import math - importar operações matematicas
#import datetime - importar data
#from datetime import date -- importar data
#from datetime import datetime

#print("O valor de pi é: ", math.pi)

#print(sys.path)

#print(datetime.datetime.now())

#data_atual = date.today()
#print(data_atual)

# importar as versoes do sistema
import platform
#importar as datas
from datetime import datetime
import modulo_igor

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')

print(data_e_hora_em_texto)


x=platform
plataforma=x.system()
print(plataforma)
print(x.python_version())
print(x.processor())


modulo_igor.boas_vindas('juan')