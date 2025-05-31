#EXERCICIO 6
'''
Faça um algoritmo que leia um número e imprima, em ordem decrescente, todos os números impares
até número 1.
'''
while True:
    n = int(input('Digite um número: '))
    if n>0:
        break
    print("O numero digitado deve ser positivo!")

if n % 2 == 0:
    for numero in range(n-1, 0, -2):
        print(numero)
else:
    for numero in range(n, 0, -2):
        print(numero)