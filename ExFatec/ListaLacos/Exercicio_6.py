'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa
de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento
'''
pop_a = 80000
cresc_a = 0.03
pop_b = 200000
cresc_b = 0.015
for ano in range(1,999999):
    pop_a += pop_a*cresc_a
    pop_b += pop_b*cresc_b
    if pop_a >= pop_b:
        print(f'Foram necessários {ano} anos para que a população de a ultrapasasse a de b')
        break
