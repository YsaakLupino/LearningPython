'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

CONTADOR = 0
idades = []
LOOP = 's'
ans = ['s', 'n']
class_class = ['Jovem', 'Adulta', 'Idosa']

while LOOP[0] == 's':
    while True:
        try:
            CONTADOR += 1
            idd = int(input(f'Insira sua idade, aluno {CONTADOR}: '))
            if not 0 < idd < 150:
                print('A idade precisa estar entre 0 e 150!')
                continue
            break
        except ValueError:
            print('Entrada inválida!')
    idades.append(idd)
    while True:
        try:
            LOOP = str(input('Deseja inserir a idade de mais um aluno?: ')).lower()
            if LOOP[0] not in ans:
                print('Responda com sim ou não!!')
                continue
            break
        except ValueError:
            print('Entrada inválida!')

mean = sum(idades)/len(idades)

print(f'A idade média da turma é {mean:.2f}')

if 0 <= mean <= 25:
    print(f'A turma é classificada como: {class_class[0]}')
if 26 <= mean <= 60:
    print(f'A turma é classificada como: {class_class[1]}')
if mean > 60:
    print(f'A turma é classificada como: {class_class[2]}')
