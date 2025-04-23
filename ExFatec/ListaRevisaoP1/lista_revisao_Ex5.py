#EXERCICIO 5
'''
Elabore um algoritmo que leia a quantidade de pessoas entrevistadas em uma pesquisa e em seguida,
o peso de cada uma. Apresente como resultado final, a média aritmética dos pesos informados.
'''

while True:
    qtd_entrevistados = int(input("Quantas pessoas foram entrevistadas? "))
    if qtd_entrevistados > 0:
        break
    print('A quantidade de entrevistados deve ser maior que zero!')

soma_peso = 0
for entrevistado in range(qtd_entrevistados):
    while True:
        peso = float(input(f'Qual o peso do entevistado número {entrevistado+1}? '))
        if peso > 0:
            break
        print('O peso da pessoa deve ser maior que zero!')
    soma_peso += peso

print(f'A média aritimética dos pesos informados é de: {soma_peso/qtd_entrevistados:.2f}')