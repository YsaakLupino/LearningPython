'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n-ésimo termo.
'''

fibbo = []

while True:
    try:
        n = int(input('Até qual termo você deseja ir com fibonacci? '))
        break
    except ValueError:
        print('Entrada inválida!')

for num in range(n):
    try:
        fibbo.append(fibbo[-1]+fibbo[-2])
    except IndexError:
        fibbo.append(1)

print(fibbo)
