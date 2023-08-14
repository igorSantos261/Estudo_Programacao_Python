#Função

def inverte_string(valor_string):
    resultado= " "

    for caracter in valor_string:
        resultado= caracter +resultado

    return resultado


string=input('Entre com uma string: ')

while string.strip()!= "":
    print("O inverso de  ", string, "é", inverte_string(string))
    string=input("Entre com outra string ou pressione ENTER para sair: ")
