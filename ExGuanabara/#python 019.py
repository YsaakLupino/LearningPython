#python 019

from random import choice

aluno  = input('Qual aluno voce quer por na lista? ')
alunos =[]
alunos.append(aluno)
loop =  input('Deseja colocar outro aluno na lista? [Sim/nao]: ').lower()

while True:
    if loop[0] == 's':
        aluno  = input('Qual aluno voce quer por na lista? ')
        alunos.append(aluno)
        loop =  input('Deseja colocar outro aluno na lista? [Sim/nao]: ').lower()
    else: 
        break

escolhido = choice(alunos)

print('o aluno que escolhido é {}'.format(escolhido))