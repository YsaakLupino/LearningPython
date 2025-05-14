#python 031
distancia = int(input("Qual a distância da sua viagem? "))
if distancia <= 200:
    print(f"Sua passagem vai custar R${distancia*0.50:.2f}")
else:
    print(f"Sua passagem vai custar R${distancia*0.45:.2f}")