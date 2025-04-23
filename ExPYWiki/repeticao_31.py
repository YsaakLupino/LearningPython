'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios
de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores referentes 
aos preços das mercadorias. Um valor zero deve ser informado pelo operador 
para indicar o final da compra. O programa deve então mostrar o total da compra 
e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e 
mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, 
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
'''
from time import sleep
ans = ['s','n']
FIRST = True
SECOND = False
while True:
    if FIRST:
        STRING = 'Inicializando programa...'
        for caract in STRING:
            print(caract, end='', flush=True)
            sleep(0.05)
        print()
    if SECOND:
        while True:
            try:
                LOOP =  str(input('Deseja passar outra compra?[S/N]' )).lower()
                if LOOP[0] not in ans:
                    print('Por favor, responda com sim ou não!')
                break
            except ValueError:
                print('Entrada inválida!')
        if LOOP[0] != 's':
            break
    FIRST = False
    SECOND = True
    P = -78
    CONTADOR = 0
    precos = []
    while P != 0:
        CONTADOR += 1
        while True:
            try:
                P = float(input(f'Digite 0 para finalizar ou o preço do produto {CONTADOR}: '))
                break
            except ValueError:
                print('Entrada inválida!')
        if P > 0:
            precos.append(P)
    print(f'O total foi de: R$ {sum(precos):>6.2f}')
    while True:
        try:
            dinheiro = float(input('Quanto o cliente deu em dinheiro? '))
            if dinheiro < sum(precos):
                print('Quantidade insuficiente de dinheiro para a compra!')
                continue
            break
        except ValueError:
            print('Entrada Inválida!')
    for produto, preco in enumerate(precos, start=1):
        print(f'Produto {produto}: R$ {preco:>6.2f}', flush='')
    print(f'Total: R$ {sum(precos):>6.2f}')
    print(f'Dinheiro: R$ {dinheiro:>6.2f}')
    print(f'Troco: R${dinheiro-sum(precos):>6.2f}')
