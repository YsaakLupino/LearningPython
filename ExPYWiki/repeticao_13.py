'''
Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
'''

while True:
    try:
        n1 = int(input('Digite a base: '))
        break
    except ValueError:
        print("Entrada Inválida")

while True:
    try:
        n2 = int(input('Digite o expoente: '))
        break
    except ValueError:
        print("Entrada Inválida")
R = 1
for n in range (1, n2+1):
    R *= n1
print(R)
