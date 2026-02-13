'''
Considere a seguinte lista de números:

numeros = [2, 5, 8, 1, 9, 4, 6, 3, 7]

a) Crie uma lista por compreensão que contenha apenas os números pares elevados ao quadrado.
'''
numeros = [2, 5, 8, 3, 1, 9, 4, 6, 3, 7]

numeros_novo = [n**2 for n in numeros if n%2 == 0]
print(numeros_novo)

'''
b) Crie um set (conjunto) com os números da lista e remova o número 1, se existir.
'''
numeros_set = set(numeros)

try:
    numeros_set.remove(1)
except KeyError:
    print('Não há numero 1')
    pass

print(numeros_set)
'''
c) Converta a lista numeros em uma tupla e exiba o último elemento.
'''

numeros_tuple = tuple(numeros)
print('O ultimo elemento da tupla', numeros_tuple, 'é', numeros_tuple[-1])

'''
d) Crie um dicionário onde as chaves sejam os valores da lista e os valores sejam seus quadrados.
'''

numeros_dict= {}
for numero in numeros:
    numeros_dict[numero] = numero**2

print(numeros_dict)