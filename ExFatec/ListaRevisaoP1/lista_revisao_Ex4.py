#EXERCICIO 4
'''
Sabendo que somente os municípios que possuem mais de 20000 eleitores aptos têm segundo turno
nas eleições para prefeito caso o
primeiro colocado não tenha mais do que 50% dos votos, fazendo um algoritmo que leia o nome do
município, a quantidade de eleitores aptos, o número de votos do candidato mais votado e informar se
ele terá ou não segundo turno em sua eleição municipal.
'''

nome_municipio = input('Digite o nome do munícipio: ')

while True:
    eleitores_municipio = int(input(f'Quantos eleitores existem em {nome_municipio}? '))
    if eleitores_municipio > 0:
        break
    print('A quantidade de eleitores tem que ser maior que zero!')

while True:
    maior_qtd_votos = int(input('Quantos votos o primeiro colocado teve? '))
    if maior_qtd_votos <= eleitores_municipio:
        break
    print('O primeiro colocado não pode ter mais votos do que a quantidade de eleitores na cidade')

if eleitores_municipio > 20000 and maior_qtd_votos < eleitores_municipio/2:
    print(f'O municipio {nome_municipio} terá segundo turno!')
else:
    print(f'O municipio {nome_municipio} não terá segundo turno!')