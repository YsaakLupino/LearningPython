#python 029

velocidade = int(input("Qual a velocidade que o carro estava? "))
velocidade_limite = 80

if velocidade > velocidade_limite:
    print(f"Você estava {velocidade-velocidade_limite}Km p/hr mais rápido do que o permitido e foi multado!")
    print("Sua multa vai custar R${:.2f}".format((velocidade-velocidade_limite)*7))
else:
    print("Você estava dentro da velocidade permitida!")