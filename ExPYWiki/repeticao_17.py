'''
Faça um programa que calcule o fatorial de um número inteiro
fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''

while True:
    try:
        n = int(input('Insira um número inteiro: '))
        break
    except ValueError:
        print('Entrada inválida!')

fatorado = 1
for num in range(n):
        fatorado *= n-num

print(fatorado)