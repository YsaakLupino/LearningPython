#EXERCICIO 3
'''
Um comerciante comprou um produto e quer vende-lo com um lucro de 45% se o valor da compra for
menor que R$ 20,00; caso contrário, o lucro será de 30%. Entrar com o valor do produto e imprimir o
valor da venda.
'''

v_produto = float(input('Digite o valor do produto: '))

if v_produto < 20:
    v_venda = v_produto * 0.45 + v_produto
    print(f'O valor da venda sera de: R${v_venda:.2f}')
    print('LUCRO DE 45%')
else:
    v_venda = v_produto * 0.3 + v_produto
    print(f'O valor da venda sera de: R${v_venda:.2f}')
    print('LUCRO DE 30%')