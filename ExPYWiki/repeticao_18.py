'''
Faça um programa que,dado um conjunto de N números, 
determine o menor valor, o maior valor e a soma dos valores.
'''

nums =[]
while True:
    while True:
        try:
            n = int(input('Insira um número inteiro: '))
            break
        except ValueError:
            print('Entrada inválida!')
    answer =['s','n']
    while True:
        try:
            loop = str(input('Deseja inserir outro número? [S/N]')).lower()
            if loop[0] not in answer:
                print('Responda com sim ou não!')
                continue
            break
        except ValueError:
            print('Entrada inválida!')
    nums.append(n)
    if loop[0] == 'n':
        break

maior = max(nums)
soma = sum(nums)
menor = min(nums)

print(f'''
O maior número que você digitou é:     {maior}
O menor número que você digitou é:     {menor}
A soma dos números que você digitou é: {soma}
''')


    