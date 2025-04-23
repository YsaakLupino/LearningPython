'''
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido.
'''

while True:
    try:
        N = int(input("Por favor, insira uma nota entre 0 e 10: "))
    except ValueError:
        print('Entrada inválida!')
        continue
    if N > 10:
        print('Entrada inválida!')
        continue
    if N < 0:
        print('Entrada inválida!')
        continue
    else:
        print('Entrada válida!')
        break
