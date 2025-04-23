'''
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''

while True:
    try:
        n1, n2, n3, n4, n5 = [int(input(f"Digite o {n+1}º numero")) for n in range(5)] #for simplificado
        break
    except FileNotFoundError:
        print('Você precisa digitar 5 numeros!')

print('n1 = {}, n2 ={}, n3 = {}, n4 = {}, n5 = {}'.format(n1, n2, n3, n4, n5))