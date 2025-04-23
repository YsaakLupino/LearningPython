'''
Faça um programa que mostre todos os primos entre 1 e N
sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões
que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''

while True:
    try:
        n = int(input('Insira um número inteiro positivo maior que 1: '))
        if n <= 1:
            print('Entrada inválida!')
            continue
        break
    except ValueError:
        print('Entrada inválida!')

prime1 = []
prime2 = []
CONTADOR = 0
for num in range(2, n+1):
    for num2 in range(1, num+1):
        if num%num2 == 0:
            prime1.append(num)
        CONTADOR += 1

for num in range(2, n+1):
    if prime1.count(num) == 2:
        prime2.append(num)

print(f'''
Entre 1 e {n} há {len(prime2)} números primos! Estes são:
{prime2}
O número de divisões feitas para encontrar essa lista de primos foi de: {CONTADOR}
''')
