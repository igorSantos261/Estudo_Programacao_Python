##Utilizando Continue e Break

i = 1 
while i < 5:
    print (i)
    i += 1
    
    if i == 4:
       break

print('############')

j = 10 
while j < 20:
    print (j)
    j += 1
    
    if i == 19:
       continue

print('############')

c = 10 
while c < 20:
    c += 1
    if c == 19:
       continue
    print (c)
    
    ###DESAFIO 5.2: PAR OU ÍMPAR
    
    print('###DESAFIO 5.2: Par OU ÍMPAR')
    
    # Mod = Pegar o Resto da divisão
    # Exemplo: 5 % 3 = 2 (resto da divisão de 5 por 3)
    
    for numero in range(20):
           if(numero % 2 == 1):
                  continue
           elif(numero == 15):
                  break
           print(numero)    
    