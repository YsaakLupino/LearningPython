'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
'''

fibbo = []
NUM_FIBBO = 0
while True:
    try:
        fibbo.append(fibbo[-1]+fibbo[-2])
    except IndexError:
        fibbo.append(1)
    NUM_FIBBO = fibbo[-1]
    if NUM_FIBBO > 500:
        fibbo.pop()
        print(fibbo)
        break
