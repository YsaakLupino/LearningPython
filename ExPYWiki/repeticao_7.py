'''
Faça um programa que leia 5 números e informe o maior número.
'''

nums = []

for n in range(5):
    while True:
        try:
            num = int(input('Insira um número inteiro: '))
            break
        except ValueError:
            print('Entrada inválida!')
    nums.append(num)

print(f'o maior número que você digitou é: {max(nums)}')
