'''
Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes
com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva
o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

PAIS_A = 80000
PAIS_B = 200000

ANO = 0
while PAIS_A < PAIS_B:
    PAIS_A = PAIS_A + PAIS_A * 0.03
    PAIS_B = PAIS_B + PAIS_B * 0.015
    ANO += 1

print(f'Levou {ANO} anos para a população do pais A alcançar a do B')
print(f'População do A: {PAIS_A:.2f}')
print(f'População do B: {PAIS_B:.2f}')
