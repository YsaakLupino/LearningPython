#EXERCICIO 7
'''
Um caixa automático precisa calcular quais e quantas notas devem ser entregues ao cliente para
efetuar a retirada desejada. Faça um algoritmo com as opções seguintes:
a. Ler o valor da retirada e mostrar a quantidade de notas de 10 e de 50 a serem entregues. Se
alguma das quantidades não for suficiente, o algoritmo cancela a operação, com uma mensagem
apropriada. (Dica: para calcular as quantidades de notas use os operadores div e mod ).
b. Apresentar um relatório com as quantidades de notas e valor total disponível, além do valor total de
retiradas efetuadas.
'''

qtd_50_total = 0
qtd_10_total = 0
retiradas = 0

while True:
    while True:
        valor_saque = int(input('Por favor, insira o valor do saque:'))
        if valor_saque > 0:
            break
        print('O valor a sacar deve ser maior que zero!')

    qtd_50 = valor_saque//50
    valor_saque_rest = (valor_saque - (qtd_50*50))
    qtd_10 = valor_saque_rest//10
    valor_saque_rest -= qtd_10*10
    error = False
    
    if valor_saque_rest > 0:
        if valor_saque_rest % 2 == 0:
            print('O caixa necessitaria de notas de dois reais para este saque!'+
            '\n Cancelando operação...')
            while True:
                loop = input('Deseja efetuar um novo saque?(sim/nao) ').lower()
                if loop == 'sim' or loop == 'nao':
                    if loop == 'sim':
                        loop = True
                    else:
                        loop = False
                    break
                print('Por favor insira \'sim\' ou \'nao\' como resposta' )
            if loop:
                continue
        if valor_saque_rest % 3 == 0:
            print('O caixa necessitaria de moedas de 1 real e notas de 2 reais para este saque!'+
                '\nCancelando operação...')
            while True:
                loop = input('Deseja efetuar um novo saque?(sim/nao) ').lower()
                if loop == 'sim' or loop == 'nao':
                    if loop == 'sim':
                        loop = True
                    else:
                        loop = False
                    break
                print('Por favor insira \'sim\' ou \'nao\' como resposta' )
            if loop:
                continue
        if valor_saque_rest % 5 == 0:
            print('O caixa necessitaria de notas de cinco reais para este saque!'+
            '\n Cancelando operação...')
            while True:
                loop = input('Deseja efetuar um novo saque?(sim/nao) ').lower()
                if loop == 'sim' or loop == 'nao':
                    if loop == 'sim':
                        loop = True
                    else:
                        loop = False
                    break
                print('Por favor insira \'sim\' ou \'nao\' como resposta' )
            if loop:
                continue
        if valor_saque_rest % 7 == 0:
            print('O caixa necessitaria de notas de dois e cinco reais para este saque!'+
            '\n Cancelando operação...')
            while True:
                loop = input('Deseja efetuar um novo saque?(sim/nao) ').lower()
                if loop == 'sim' or loop == 'nao':
                    if loop == 'sim':
                        loop = True
                    else:
                        loop = False
                    break
                print('Por favor insira \'sim\' ou \'nao\' como resposta' )
            if loop:
                continue
        if valor_saque_rest == 9 or valor_saque_rest == 1:
            print('O caixa necessitaria de moedas de 1 real ou notas de 2 e 5 reais para este saque!'+
                '\nCancelando operação...')
            while True:
                loop = input('Deseja efetuar um novo saque?(sim/nao) ').lower()
                if loop == 'sim' or loop == 'nao':
                    if loop == 'sim':
                        loop = True
                    else:
                        loop = False
                    break
                print('Por favor insira \'sim\' ou \'nao\' como resposta' )
            if loop:
                continue
        error = True
    if not error:
        print(f'A quantidade de notas de 50 neste saque é: {qtd_50}'+
            f'\nA quantidade de notas de 10 neste saque é {qtd_10}')
        qtd_10_total += qtd_10
        qtd_50_total += qtd_50
        retiradas += 1
        valor_total_disponivel = qtd_10_total * 10 + qtd_50_total * 50

        while True:
            loop = input('Deseja efetuar um novo saque?(sim/nao) ').lower()
            if loop == 'sim' or loop == 'nao':
                if loop == 'sim':
                    loop = True
                else:
                    loop = False
                break
            print('Por favor insira \'sim\' ou \'nao\' como resposta' )
        if loop:
            continue

    print('*'*5+'RELATÓRIO'+'*'*5)
    print(f'A quantidade total de notas de 50 sacadas é de: {qtd_50_total}'
            f'\nA quantidade total de notas de 10 sacadas é de: {qtd_10_total}'
          f'\nO numero de saques efetuados com sucesso foi de: {retiradas}'
          f'\nO valor total disponivel com você é de: {valor_total_disponivel}'
          )
    print('Obrigado por ultilizar nosso sistema de saque! Até mais!')
    quit()
