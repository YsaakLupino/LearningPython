'''
Faça um programa que peça um número inteiro e determine
se ele é ou não um número primo. Um número primo é
aquele que é divisível somente por ele mesmo e por 1.
'''

while True:
    try:
        n = int(input('Por favor insira um número inteiro e maior que 1: '))
        if n <= 1:
            print('Entrada inválida!')
            continue
        break
    except ValueError:
        print('Entrada inválida!')

prime = []
for num in range(1, n+1):
    if n%num == 0:
        prime.append(num)

if len(prime) == 2:
    print(f'O número que você digitou({n}) é um número primo!')
else:
    print(f'O número que você digitou ({n}) não é um número primo!')
