#EXERCICIO 8
'''
Faça algoritmos, utilizado laços, que imprimam as figuras a seguir.
linha : Usuário informa a base
'''
while True:
    base = int(input('Informa e base do tringualo invertido a ser impresso usando \'*\''))
    if base > 0:
        break
    print('O numero informado deve ser maior que zero!')

print('*'*base)
        