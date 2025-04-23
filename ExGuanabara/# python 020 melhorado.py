# python 020

from random import shuffle
from time import sleep

alunos = []
alunos.append(str(input('Qual o nome do aluno que deseja inserir na lista de apresentação? ')))
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.',)
print('Aluno adicionado na lista!')
sleep(0.5)

loop = str(input('Deseja adicionar outro aluno? [S/N]')).lower()

while loop[0] == 's':
    alunos.append(str(input('Qual o nome do aluno que deseja inserir na lista de apresentação? ')))
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.',)
    print('Aluno adicionado na lista!')
    sleep(0.5)
    loop = str(input('Deseja adicionar outro aluno? [S/N]')).lower()

shuffle(alunos)

posicao = 0
print('A ordem de apresentação será: ')
for aluno in alunos:
    posicao += 1 
    print("{} - {}".format(posicao, aluno))
    
