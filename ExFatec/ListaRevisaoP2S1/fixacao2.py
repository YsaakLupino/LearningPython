'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na 
ordem inversa.'''

vetor_num = []
for n in range(10):
    while True:
        try:
            
            n = int(input('Insira um numero: '))
            break
        except ValueError:
            print('Precisa inserir um número inteiro!')
    vetor_num.append(n)



print(vetor_num[::-1])