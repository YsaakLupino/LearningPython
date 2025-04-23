def imprimir_estiloso(n):
    printado = n - n + 1
    while printado <= n:
        for num in range (printado):
            num+=1
            print(f"{num} ", end="")
        print()
        printado += 1

imprimir_estiloso(5)

