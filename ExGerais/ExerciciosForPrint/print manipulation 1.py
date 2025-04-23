def imprimir_loop(numero):
    for i in range(numero):
        loop = i+1
        print(f"{loop} " * loop)



numero_escolhido = int(input("Insira um número: "))
imprimir_loop(numero_escolhido)