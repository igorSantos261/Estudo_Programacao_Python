#Tomada de decisão aninhada IF aninhado

'''altura=int(input("Favor inserir a sua altura em centimetro: "))

if(altura<150) or (altura>180):
    print('Voce nao pode usar o brinquedo')

else:
    print('Voce tem altura para usar o brinquedo')'''

#Programa if com escolha

x=float(input('Entre com o primeiro numero: '))
y=float(input('Entre com o segundo numero: '))

print('***MENU ESCOLHA***')
print('1- soma dos valores')
print('2- subtracao dos valores')
print('3- multiplicacao dos valores')
print('4- divisao dos valores')


escolha=int(input('Escolha um dos valores: '))


print('O resultado eh: ', end='')

if(escolha==1):
    print(x+y)
else:
    if(escolha==2):
        print(x-y)
    else:
        if(escolha==3):
            print(x*y)
        else:
            if(escolha==4):
                print(x/y)
            else:
                print('Opcao invalida! ')


