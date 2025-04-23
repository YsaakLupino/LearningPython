'''
Faça um programa que receba dois números inteiros e gere os
números inteiros que estão no intervalo compreendido por eles.
'''

while True:
    try:
        n1 = int(input('Digite o primeiro número: '))
        break
    except ValueError:
        print("Entrada Inválida")

while True:
    try:
        n2 = int(input('Digite o segundo número: '))
        break
    except ValueError:
        print("Entrada Inválida")
nums = [n1, n2]
for num in range (min(nums), max(nums)+1):
    print(num, flush= True, end="")
    if num == max(nums):
        print(".")
        break
    print('; ', flush= True, end="")
