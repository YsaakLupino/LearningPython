from time import sleep

def imprimir_loop(numero):
    referencia = []
    for n in range(numero):
        referencia.append(n+1)
    for n in referencia:
        loop = n - n + 1
        while loop <= n:
            print(f"{loop} ", end="", flush=True)
            sleep(0.10)
            loop += 1
            if loop > n:
                print('\n')


numero_escolhido = int(input("Insira um número: "))
imprimir_loop(numero_escolhido)

