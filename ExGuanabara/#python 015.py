#python 015

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km o locatário andou com o carro? '))
custo = dias*60+km*0.15

print('O carro foi alugado por {} dias, deslocou por {} Km, e o valor a pagar é de R${}'.format(dias, km, custo))