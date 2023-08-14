#Conjunto de Dados


conjunto_a=set([1,2,3])
conjunto_b=set([3,4,5])

print(conjunto_a)
print(conjunto_b)

#uniao

uniao=conjunto_a.union(conjunto_b)
print('Uniao AUB = ',uniao)

#intersecção
interseccao=conjunto_a.intersection(conjunto_b)
print('Intersecção A e B = ',interseccao)


#Diferença
diferenca=conjunto_a.difference(conjunto_b)
print('diferença do conjunto A e B = ',diferenca)

#Diferença simetrica

diferenca_simetrica=conjunto_a.symmetric_difference(conjunto_b)
print('diferença simetrica do conjunto A e B = ',diferenca_simetrica)
