#python 032

ano = int(input("Digite um ano para verificar se é bissexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0):
    print("Esse é um ano bissexto")
else:
    print("Esse não é um ano bissexto")
 
