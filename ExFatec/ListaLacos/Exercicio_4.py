'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois
modifique o programa para que ele mostre os números um ao lado do outro.
'''

# etapa 1 
for n in range(1, 20+1):
    print(n)

# etapa 2 
for n in range(1, 20+1):
    print(f'{n} ', end='')