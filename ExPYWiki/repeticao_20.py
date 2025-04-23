'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular
o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''

answers =['s', 'n']
LOOP = 's'
while LOOP[0] == 's':
    while True:
        try:
            n = int(input('Insira um número inteiro: '))
            if not 0 < n < 16:
                print('Por favor insira um número positivo e menor que 16!')
                continue
            break
        except ValueError:
            print('Entrada inválida!')

    FATORADO = 1
    for num in range(n):
        FATORADO *= n-num

    print(FATORADO)

    while True:
        try:
            LOOP = str(input('Deseja fazer outro cálculo de fatoriral? [S/N]')).lower()
            if LOOP[0] not in answers:
                print('Responda com SIM ou NÃO!')
                continue
            break
        except ValueError:
            print('Entrada inválida')
