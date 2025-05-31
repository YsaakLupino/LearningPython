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
    
esp = 0
for n in range (base, 0, -1):
    if n == base:
        print('*'*(n*2))
    if n != base:
        esp += 2
        print('*'*n+' '*esp+'*'*n)
esp = 2*base
for n in range (1, base+1):
    if n == base:
        print('*'*(n*2))
    if n != base:
        esp -= 2
        print('*'*n+' '*esp+'*'*n)
