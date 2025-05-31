#EXERCICIO 8
'''
Escrever um algoritmo que calcula e escreve a soma de todos os números primos entre 92 e 1478.
Número primo é aquele que só pode ser divisível por 1 e ele mesmo.
'''

soma = 0
for n in range (93, 1479):
    div = 0
    for y in range(1, n+1):
        if n % y == 0:
            div += 1
        if div > 2:
            break
    if div == 2:
        soma += n
print(soma)
        