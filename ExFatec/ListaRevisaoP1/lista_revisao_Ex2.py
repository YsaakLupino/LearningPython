#EXERCICIO 2
'''
Criar o algoritmo que deixe entrar com dois números e imprimir o quadrado do menor número e a raiz
quadrada do maior número, se for possível.
'''

while True:
    n1 = int(input('Digite um número:'))
    n2 = int(input('Digite outro número:'))
    if n1 != n2:
        break
    print('os número inseridos devem ser diferentes!')

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

print(f'O quadrado do menor número digitado({menor}) é: {menor**2}!')
if maior < 0: 
    print(f'Impossível calcular a raiz quadrada do maior número digitado({maior}) pois ele é negativo!')
else:
    print(f'A raíz quadrada do maior número({maior}) é: {maior**0.5}!')
