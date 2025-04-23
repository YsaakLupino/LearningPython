#EXERCICIO 1
'''
Ler um número de 4 casas (MCDU) e imprimir se é ou não múltiplo de quatro o número formado pelos
algarismos que estão nas casas das unidades de milhar e das centenas.
'''

while True:
    n = int(input('Digite um número com quatro algarismos: '))
    if n>=1000 and n<10000:
        break
    print('Por favor insira um numero maior ou igual a 1000 ou menor que 10000')

primeiros_dois = n//100

print(f'Os dois primeiros algarismo de {n} formam {primeiros_dois}!')

if primeiros_dois % 4 == 0:
    print(f'Sim! {primeiros_dois} é múltiplo de 4!')
else:
    print(f'Não! {primeiros_dois} não é múltiplo de 4!')

