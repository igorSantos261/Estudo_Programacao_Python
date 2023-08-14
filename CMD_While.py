Contador = 1

while Contador < 6:
    print(Contador)
    Contador +=1
    
    
    
condicao_de_parada = '0'

while condicao_de_parada != '9':
    condicao_de_parada = input('Digite um Numero: ')
    for i in range (1,int(condicao_de_parada)+1):
        print(i)
    
