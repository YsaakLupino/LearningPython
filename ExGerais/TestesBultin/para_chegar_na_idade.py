print("Seja bem vindo ao meu programa teste!!! ",
      "\nAqui você vai poder digitar um número e ver quanto falta pra chegar na sua idade!! ",
      "\n-------------------------------------------------------------------------------------",
      "\nCaso o número seja maior, não será calculado e você será avisado!")

error_txt = "Você digitou uma letra, por favor, digite um número inteiro!".upper()
N = -121265436546531354665164777987989931
while N == -121265436546531354665164777987989931:
    try:
        N = int(input("Digite um número inteiro para prosseguir ou *SAIR* para finalizar o programa: \nR:"))
    except ValueError:
        N = -121265436546531354665164777987989931
        print(error_txt)
        continue
    I = -121265436546531354665164777987989931
    while I == -121265436546531354665164777987989931:
        try:
            I = int(input("Digite sua idade: "))
        except ValueError:
            I = -121265436546531354665164777987989931
            print(error_txt)
            continue
verde = "\033[1;32;40m"
print(f"{verde}Você escolheu o número: ", N)
print(f"{verde}Sua idade é: ", I)
print("\n")
if N>I:
    print("Você escolheu um número maior que sua idade. Resultado impossível!")
else:
    print("Partindo do", N, "Faltam", I-N, "Para chegar na sua idade", I)
