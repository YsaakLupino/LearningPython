'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
from statistics import mean
nums = []
for n in range(5):
    while True:
        try:
            num = int(input('Por favor insira um número inteiro!'))
            break
        except ValueError:
            print('Entrada inválida!')
    nums.append(num)
MEDIA = mean(nums)

print(f'A soma dos números que você digitou é: {sum(nums)}')
print(f'A média dos números que você digitou é: {MEDIA}')
