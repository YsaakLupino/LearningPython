'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
'''

while True:
    try:
        n = int(input('Inisira o número que deseja a tabuada: '))
        break
    except ValueError:
        print('Entrada inválida!')


# sem estrtutura de repeticao
print(f'''
1  x {n}   =  {1*n}
2  x {n}   =  {2*n}
3  x {n}   =  {3*n}
4  x {n}   =  {4*n}
5  x {n}   =  {5+n}
6  x {n}   =  {6*n}
7  x {n}   =  {7*n}
8  x {n}   =  {8*n}
9  x {n}   =  {9*n}
10 x {n}   =  {10*n}
''')

#com estrtutra de repeticao
for num in range(0, 11):
    print(f"{num:<4}X {n:^5}={n*num:4}")
