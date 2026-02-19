'''
1. Escreva um programa em Python que: 
a)  Leia do usuário uma sequência de números inteiros separados por espaço e 
armazene-os em uma lista. 
b)  Realize as seguintes operações: 
i. Exiba a lista original. 
ii. Crie uma nova lista apenas com os números pares, mantendo a ordem original. 
iii. Crie outra lista com os elementos da lista original sem o primeiro e o último 
elemento (use fatiamento). 
iv. Calcule a média dos valores da lista original e exiba. 
v. Encontre o segundo maior valor da lista original.

c) Mostre todas as listas e os resultados calculados. 
'''
'''

# 1.A)
lista_ = str(input('Digite uma sequencia inteiros de numeros separados por espaço'))
lista_ = lista_.split(" ")
lista_= [int(n) for n in lista_]
# 1.B)
print(lista_)
# 1.C)
lista_par = [n for n in lista_ if n%2 == 0 ]
# 1.D)
lista_fatiada = lista_[1:-1]
#1.E)
lista_mean = sum(lista_)/len(lista_)
# 1.F)
lista_.sort()
lista_second = lista_[-2]
print(lista_second)
# C)
print(f'Lista original: {lista_}\n'+
      f'Lista fatiada: {lista_fatiada}\n'
      f'Lista par: {lista_par}\n'
      f'Média da lista: {lista_mean}\n'
      f'Segundo maior item: {lista_second}\n'     
      )
'''

'''
2. Peça ao usuário para digitar uma lista de números inteiros separados por espaço e: 
a)  Converta-os para uma lista de inteiros. 
b)  Crie, usando list comprehension, uma nova lista contendo o quadrado de cada número 
da lista original. 
c) Exiba as duas listas. 
Exemplo de entrada e saída: 
Entrada: 2 3 4 
Saída: [4, 9, 16]
'''
'''
lista_ = str(input('Digite uma sequencia inteiros de numeros separados por espaço'))
lista_ = lista_.split(" ")
lista_= [int(n) for n in lista_]
lista_powered = [pow(n,exp=2) for n in lista_]
print(lista_)
print(lista_powered)
'''

'''
3. Peça ao usuário para digitar uma frase qualquer e: 
a)  Separe as palavras da frase em uma lista. 
b)  Usando list comprehension, crie uma nova lista contendo apenas as palavras com mais 
de 4 letras. 
c) Exiba as duas listas.
'''
'''
frase = str(input('Digite uma frase qualquer: '))
lista_frase = frase.split(' ')
lista_frase_menor4 = [n for n in lista_frase if len(n)>4]
print(lista_frase_menor4)
print(lista_frase)
'''

'''
4. Peça ao usuário para digitar um texto qualquer e: 
a)  Separe todas as palavras do texto em uma lista (considere que as palavras são separadas 
por espaço). 
b)  Converta essa lista em um set, para obter apenas as palavras únicas (eliminando 
repetições). 
c) Exiba: 
• A quantidade de palavras diferentes no texto. 
• A lista das palavras únicas em ordem alfabética. 
 
Exemplo de entrada e saída: 
 
Entrada: "Python é divertido e Python é poderoso" 
Palavras únicas: {'Python', 'é', 'divertido', 'e', 'poderoso'} 
Quantidade: 5 
Em ordem: ['Python', 'divertido', 'e', 'poderoso', 'é'] 
'''

'''
frase = str(input('Digite uma frase qualquer: '))
lista_frase = frase.split(' ')
lista_frase = set(lista_frase)
print(f'Quantidade = {len(lista_frase)}')
print(sorted(lista_frase))
'''