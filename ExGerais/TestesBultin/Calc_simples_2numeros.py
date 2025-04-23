pintar = '\033[1;30;41m'
despintar = '\033[0m'
def main():
    while True:
        try:
            n1 = float( input('Insira o primeiro numero da sua operação: ') )
            break
        except:
            print(f"{pintar}Você precisa inserir um número válido!{despintar}") 

    while True:
        try:
            n2 = float( input('Insira o segundo numero da sua operação: ') )
            break
        except: 
            print(f"{pintar}Você precisa inserir um número válido!{despintar}") 

    print("Digite o número da opção escolhida:")

    debug = 0
    while debug == 0:
        try:
            operacao = int(input ('Qual a operação que voce deseja fazer?\n' + 
                                '(1) Adição\n' +
                                '(2) Subtração\n' +
                                '(3) Multiplicação\n' +
                                '(4) Divisão\n' +
                                'Escolha uma opção: '
                                ) )
            debug = 1
        except ValueError:
            print(f'{pintar}Por favor insira apenas o número correspondente à opçao!{despintar}')

    debug = False

    while operacao > 4 or operacao < 0:
        if debug == True:
            print(f'{pintar}Por favor insira apenas o número correspondente à opçao!{despintar}')
        elif debug == False:
            print(f'{pintar}Por favor, escolha um número equivalente às opções{despintar}')
        
        try:
            debug == False
            operacao = int(input ('Qual a operação que voce deseja fazer?\n' + 
                                '(1) Adição\n' +
                                '(2) Subtração\n' +
                                '(3) Multiplicação\n' +
                                '(4) Divisão\n' +
                                'Escolha uma opção: '
                                )                                    )
        except ValueError:
            debug = True
            pass
    # nomeando a operação
    if operacao == 1:
        conta = "Adição"
    elif operacao == 2:
        conta = "Subtração"
    elif operacao == 3:
        conta = "Multiplicação"
    else:
        conta = "Divisão"


    #fazendo a conta 
    if n2 != 0:
        if operacao == 1:
            r = n1+n2
        elif operacao == 2:
            r = n1-n2
        elif operacao == 3:
            r = n1*n2
        elif operacao == 4:
            r = n1/n2
        
    else:
        while True:
            try:
                r = n1/n2
                break
            except ZeroDivisionError:
                print("Não dá pra dividir por zero, por favor escolha outro número")
                n2 = float( input('Insira o segundo numero da sua operação: ') )

    print(f"O resultado da {conta} de {n1} por {n2} é de {r}")

main()

loop = input('Deseja realizar outro calculo? [S/N]: ').lower()

while loop[0] == "s":
    main()
    loop = input('Deseja realizar outro calculo? [S/N]: ').lower()

print('Obrigado por usar a calculadora!')