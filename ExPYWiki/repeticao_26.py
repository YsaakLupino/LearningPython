'''
Faça um programa que receba dois números inteiros e gere
os números inteiros que estão no intervalo compreendido por eles.
'''

while True:
    try:
        n1 = int(input('Insira o primeiro número: '))
        break
    except ValueError:
        print('Entrada inválida!')

while True:
    try:
        n2 = int(input('Insira o primeiro número: '))
        break
    except ValueError:
        print('Entrada inválida!')

nums = [n1, n2]

for n in range(min(nums), max(nums)+1):
    print(f'{n}', flush = True, end="")
    if n ==  max(nums):
        print('.')
        break
    print(', ', flush = True, end= "")
    
