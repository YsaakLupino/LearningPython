#python 019 2

from random import choice

alunos =[]
alunos.append(input('Qual o primeiro aluno que voce quer por na lista? '))
alunos.append(input('Qual o segundo aluno que voce quer por na lista? '))
alunos.append(input('Qual o terceiro aluno que voce quer por na lista? '))
alunos.append(input('Qual o quarto aluno que voce quer por na lista? '))

escolhido = choice(alunos)
escolhido = escolhido[0].upper()+escolhido[1:]

print('O aluno escolhido foi: {}'.format(escolhido))




