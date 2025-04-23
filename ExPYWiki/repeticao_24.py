'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''

LOOP = 's'
resp = ['s', 'n']
grades = []
while LOOP[0] == 's':
    while True:
        try:
            GRD = int(input('Inisira a nota: '))
            break
        except ValueError:
            print('Entrada inválida!')
    grades.append(GRD)
    while True:
        try:
            LOOP = str(input('Deseja inserir outra nota?[S/N]: ')).lower()
            if LOOP[0] not in resp:
                print('Responda com sim ou não!')
                continue
            break
        except ValueError:
            print('Entrada inválida!')

MEAN = sum(grades)/len(grades)

print(f'A média das notas que você digitou é: {MEAN}')
