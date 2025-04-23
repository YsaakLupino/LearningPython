'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

nums =[]
while True:
    while True:
        try:
            n = int(input('Insira um número inteiro: '))
            if not 0 <= n <= 1000:
                print('Você só pode inserir números entre 0 e 1000')
                continue
            break
        except ValueError:
            print('Entrada inválida!')
    answer =['s','n']
    while True:
        try:
            LOOP = str(input('Deseja inserir outro número? [S/N]')).lower()
            if LOOP[0] not in answer:
                print('Responda com sim ou não!')
                continue
            break
        except ValueError:
            print('Entrada inválida!')
    nums.append(n)
    if LOOP[0] == 'n':
        break

maior = max(nums)
soma = sum(nums)
menor = min(nums)

print(f'''
O maior número que você digitou é:     {maior}
O menor número que você digitou é:     {menor}
A soma dos números que você digitou é: {soma}
''')
