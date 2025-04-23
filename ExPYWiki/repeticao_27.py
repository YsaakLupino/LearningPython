'''
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
'''

while True:
    try:
        turmas = int(input('Quantas turmas tem na escola? '))
        break
    except ValueError:
        print('Entrada inválida!')
qtd_alunos = []

for n in range(1, turmas+1):
    while True:
        try:
            qtd_sala = int(input(f'Quantos alunos tem a turma {n}? '))
            if qtd_sala > 40 or qtd_sala <= 0:
                print('A sala nao pode ter nenhum aluno ou mais de 40 alunos!!')
                continue
            break
        except ValueError:
            print('Entrada inválida!')
    qtd_alunos.append(qtd_sala)

mean = sum(qtd_alunos)/len(qtd_alunos)
print(f'A quantidade média de alunos por sala é de {mean:.2f}!!')
