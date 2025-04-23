'''1. Quadrado dos Números
Crie uma função lambda que receba um número e retorne o seu quadrado.
Teste-a com alguns valores.
'''

#squad = lambda x: x**2
#print(squad(2))




'''
2. Verificação de Número Par
Crie uma função lambda que receba um número e retorne True se for par e False caso contrário.

'''

#parity = lambda x :  x%2 == 0
#print(parity(6))

'''
3. Ordenação de Lista de Tuplas
Dada a lista de tuplas abaixo, ordene-a pelo segundo valor de cada tupla usando sorted() e uma função lambda.

lista = [(1, 4), (3, 2), (5, 9), (2, 7)]
Saída esperada: [(3, 2), (1, 4), (2, 7), (5, 9)]
'''
lista = [(1, 4), (3, 2), (5, 9), (2, 7)]

print(sorted(lista, key=1))
