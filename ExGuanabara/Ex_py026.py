#python 010

n = float(input('Quantos reais voce tem na carteira?'))
cotacao = float(3.27)

print('Com o dinheiro que voce tem na carteira, na cotação atual de {}, você consegue comprar {:.2f} dólares'.format(cotacao, n/cotacao))