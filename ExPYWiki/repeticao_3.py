'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
from time import sleep

num = [str(1), str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9), str(0)]

while True:
    NOME = str(input('Por favor insira um nome: '))
    for numero in num:
        if numero in NOME:
            NOME = False
            print(f"O nome escolhido com o número {numero}. O nome nao pode conter números")
            break
    if not NOME:
        continue
    if len(NOME) <= 3:
        print('O nome precisa conter mais de 3 caracteres!')
        continue
    break

while True:
    IDADE = int(input('Por favor insira sua idade: '))
    if 0 < IDADE <= 150:
        break
    print('Idade tem que estar entre 0 e 150')

while True:
    SALARIO = float(input('Por favor, insira seu salário: '))
    if SALARIO > 0:
        break
    print('O salário precisar ser maior que R$ 0,00')

generos = ['f', 'm']
while True:
    SEXO = str(input('Por favor, insira seu gênero: ')).lower()
    if SEXO[0] in generos:
        break
    print('Digite um gênero válido (MASCULINO / FEMININO)')

if SEXO[0] == 'f':
    SEXO = 'Feminino'
else:
    SEXO = 'Masculino'

estados_civis = ['s', 'c', 'v', 'd']
while True:
    ESTADO_CIVIL = str(input('Qual seu estado civil?\n' +
                      '(Solteiro / Casado / Divorciado / Viúvo)\nR: ')).lower()
    if ESTADO_CIVIL[0] in estados_civis:
        break
    print('Digite um estado civil válido!\n(Solteiro / Casado / Divorciado / Viúvo)')

if ESTADO_CIVIL[0] == 's':
    ESTADO_CIVIL = 'Solteiro'

elif ESTADO_CIVIL[0] == 'c':
    ESTADO_CIVIL = 'Casado'

elif ESTADO_CIVIL[0] == 'v':
    ESTADO_CIVIL = 'Viúvo'

else:
    ESTADO_CIVIL = 'Divorciado'

CARREGAR = 'Carregando...'
for caract in CARREGAR:
    print(caract, flush=True, end='')
    sleep(0.35)

print(f'Olá {NOME}!\nVocê tem {IDADE} anos, recebe R${SALARIO:.2f}, seu gênero é {SEXO} e, '+
       f'atualmente, você está {ESTADO_CIVIL}!')
