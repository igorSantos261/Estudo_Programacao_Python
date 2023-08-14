#Lista em Python
lista = []
print("Lista Vazia")
print(lista)
print(type(lista))

#Lista com valores 
lista = ['Igor','Bruna','Juan','Ivy']
print("Lista preenchida :")
print(lista[0])
print(lista[2])


#Inserindo novos valores a Lista

lista2 = [1,2,3,4]
print("Lista na sequencia", lista2)

#Incluindo valor de numero 5 
lista2.append(5)
print("Lista na sequencia", lista2)


#Lista com cores
lista3 = []

lista3.append('Azul')
lista3.append('Verde')
lista3.append('Amarelo')
lista3.append('Branco')

print(lista3)


#Lista com insert
lista3.insert(2,'preto')
lista3.insert(1,'Roxo')
print(lista3)

#lista de valores aninhado
lista4 = ['igor','Bruna','Juan','Ivy',['100','200','300','400']]

#Acessando o terceiro item da posicao dois
print(lista4)
print('O quarto item da posicao dois eh:')
print(lista4[4][2])

