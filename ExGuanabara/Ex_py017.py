#python 26

frase = str(input("Digite uma frase: ")).strip().lower()
vezes_a = frase.count("a")
primeiro_a = frase.find("a")
ultimo_a = frase.rfind("a")

print(f"""
Quantas vezes aparece a letra a: {vezes_a}
Em que posição ela aparece primeiro: {primeiro_a}
Em que posição ela aparece por útlimo:{ultimo_a}
""")

