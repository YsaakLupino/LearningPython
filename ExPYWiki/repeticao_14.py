'''
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares
e a quantidade de números impares.
'''

nums = []

for n in range(10):
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
            break
        except ValueError:
            print('Entrada inválida!')
    nums.append(num)

odds = []
pairs = []

for num in nums:
    if num%2 != 0:
        odds.append(num)
    else:
        pairs.append(num)

print(f'Você digitou {len(odds)} números ímpares')
print(f'Você digitou {len(pairs)} números pares')
