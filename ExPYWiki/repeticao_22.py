'''
Altere o programa de cálculo dos números primos, 
informando, caso o número não seja primo, por quais número ele é divisível.
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
    print('Isso por que, além de um e ele mesmo, ele também é divisível por: ')
    prime.remove(1)
    prime.remove(n)
    print(prime)
