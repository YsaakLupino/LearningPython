#python 022
nome = str(input("Insira seu nome: ")).strip()

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_cont_sem_espaço = len(nome.replace(" ", ""))
posição_primero_espaço = nome.find(" ")
nome_cont_primeiro_nome = len(nome[:posição_primero_espaço])


print(f"""
Nome maiúsculo:{nome_maiusculo}
Nome minúsculo: {nome_minusculo}
Total de letras sem espaço: {nome_cont_sem_espaço}
Total de letras do primeiro nome: {nome_cont_primeiro_nome}
""")
