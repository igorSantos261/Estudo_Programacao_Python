#Atribuicao de valores

cateto_a=5
endereco=id(cateto_a)
print(endereco)

hexa_endereco=hex(endereco)
print(hexa_endereco)


a=261
print(a)
print(id(a))


b=261
print(b)
print(id(b))


id(a)==id(b)


a = 10
b = a
print(a)
print(b)
id(a)==id(b)


i= 261
print("Tipo de dados de i", (type)(i))

j= 5.2
print("Tipo de dados de i", (type)(j))

#tipo de dados String

String1 =         '''(- . -)
                kkkkk'''
                
print(String1)    


String2 = "igoranselmosantos"
print("String eh" )
print(String2)


print("O quarto caracter eh ")
print(String2[4])