#python 27

nome = str(input('Insira um nome completo: ')).strip()
print(f"O primero nome é: {nome.split()[0]}")
print(f"O ultimo nome é: {nome.split()[-1]}")
