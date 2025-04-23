#EXERCICIO 8
'''
Faça algoritmos, utilizado laços, que imprimam as figuras a seguir.
Triângulo invertido seguido de outro não invertido.
'''

while True:
    base = int(input('Informa e base do tringualo invertido a ser impresso usando \'*\''))
    if base > 0:
        break
    print('O numero informado deve ser maior que zero!')

for n in range (base, 0, -1):
    if n != 1:
        print('*'*n)
    else:
        print('*'*n,end='')
for n in range (0, base+1):
    print('*'*n)