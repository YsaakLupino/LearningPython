'''
Faça um programa que calcule o valor total investido por um colecionador
em sua coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''

while True:
    try:
        CDS = int(input('Insira a quantidade de CDs que você tem: '))
        if CDS <= 0:
            print('A quantidade de cds tem que ser maior que zero!')
            continue
        break
    except ValueError:
        print('Entrada inválida!')

valores = []
for cd in range(1, CDS+1):
    while True:
        try:
            valor = int(input(f'Qual o valor gasto no CD {cd}: '))
            if valor <= 0:
                print('O preço tem que ser maior que zero!')
                continue
            break
        except ValueError:
            print('Entrada inválida!')
    valores.append(valor)

mean = sum(valores)/CDS

print(f'''
O total investido foi de: R$ {sum(valores):.2f}
A média de gasto com os cds é de: R$ {mean:.2f}
''')
