
#Codigo 01

'''
idade = int(input("Entre com sua Idade: "))
nova_idade = idade + 1
print("No proximo ano voce tera :{} anos".format)(nova_idade)
'''


#Codigo 02 
'''
lado_a=35
lado_b=14.33333
area_do_retangulo= (lado_a)*(lado_b)
print('O retangulo do Lado A = %d e Lado b = %.2f eh %.3f'%(lado_a,lado_b,area_do_retangulo))
'''

#Codigo 03
'''
lista_1 = [1,2,'IGTI']
lista_2 = [2,3, "Bootcamp"]
lista_3 =lista_1 + lista_2
print(lista_3)
'''

#Codigo 04

chute=int(input('Entre com um valor inteiro de 0 a 30 :'))
adivinhacao=[5,6,10,14,16,20,30]
if chute in adivinhacao:
    print('Voce acertou um dos numeros que eu estava pensando.')

    if chute > 15:
        print('Esse numero eh maior do que 20.')

    if chute < 20:
        print('Esse numero eh menor do que 20.')
    print('Voce eh fera.')
else:
    print('Que pena, voce errou. Pode tentar outra vez.')
print('Obrigado por participar!')

