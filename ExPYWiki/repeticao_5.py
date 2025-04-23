'''
Altere o programa anterior permitindo ao usuário informar as populações
e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

REP = 'Sim'.lower()
while REP[0] == 's':
    while True:
        try:
            PAIS_A = int(input('Qual o tamanho da população do pais A? '))
            break
        except ValueError:
            print('Dado inválido, digite um número inteiro!')

    while True:
        try:
            PAIS_B = int(input('Qual o tamanho da população do pais B? '))
            break
        except ValueError:
            print('Dado inválido, digite um número inteiro!')

    while True:
        try:
            CRESCIMENTO_PAIS_A = float(input('Qual a taxa de crescimento da população do país A? '))
            break
        except ValueError:
            print(r'Dado inválido, digite um número decimal que representa a % escolhida!')

    while True:
        try:
            CRESCIMENTO_PAIS_B = float(input('Qual a taxa de crescimento da população do país B? '))
            break
        except ValueError:
            print(r'Dado inválido, digite um número decimal que representa a % escolhida!')

    ANO = 0
    while True:
        if PAIS_A < PAIS_B:
            while PAIS_A < PAIS_B:
                PAIS_A = PAIS_A + PAIS_A * CRESCIMENTO_PAIS_A
                PAIS_B = PAIS_B + PAIS_B * CRESCIMENTO_PAIS_B
                ANO += 1
            break

        if PAIS_B < PAIS_A:
            while PAIS_B < PAIS_A:
                PAIS_A = PAIS_A + PAIS_A * CRESCIMENTO_PAIS_A
                PAIS_B = PAIS_B + PAIS_B * CRESCIMENTO_PAIS_B
                ANO += 1
            break

    print(f'Levou {ANO} anos para a população do menor pais alcançar o maior!')
    print(f'População do A: {PAIS_A:.2f}')
    print(f'População do B: {PAIS_B:.2f}')

    REP = str(input('Deseja repetir a operação?[S/N]: ')).lower()
