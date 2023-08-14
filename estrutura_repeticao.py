# Estrutura de Repetição

s = 'como vai você ?'

nova_string=s.upper()
print(nova_string)


i=(input('Entre com seu nome :'))
b=(input('Entre com o nome da sua esposa :'))

if i<=b:
    print('Seu nome vem antes !!')
else:
    print('Seu nome vem depois do da sua esposa')

#Estutura com FOR

string=input('Entre com um caracter :')

for caracter in string:
    print(string)
print('...FIM...')


#estrutura for com lista
lista=['igor', 'Bruna', 'juan', 'zack']

for elementos in lista:
    print(lista)
print('...FIM...')