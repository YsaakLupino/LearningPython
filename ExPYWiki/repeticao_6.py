'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.
'''

#Um abaixo do outro!
N = 0
while N < 20:
    N += 1
    print(f'Número: {N}')

#Um ao lado do outro!

N = 0
CTRL = 20
while N < CTRL:
    N += 1
    print(f'{N}', flush= True, end= "")
    if N == CTRL:
        print('.')
        break
    print('; ', flush= True, end="")
