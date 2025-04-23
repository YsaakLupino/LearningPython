

def fatorar(fatorando):
    r_total = 0
    for i in range(fatorando):
        fator = i+1
        r_parcial = fatorando-i * (fatorando-fator)
        r_parcial
    return r_total


while True:
    try:
        numero = int(input("Qual número você deseja fatorar? "))
        break
    except:
        print('Insira um número inteiro válido')

if numero == 0 or numero < 0:
    while True:
        print('Insira um número inteiro positivo e diferente de 0')
        numero = int(input("Qual número você deseja fatorar? "))
        if numero == 0 or numero < 0:
            pass
        else:
            break

R = fatorar(numero)
print(R)

