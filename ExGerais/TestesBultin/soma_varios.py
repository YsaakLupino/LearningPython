Vd_Bk = "\033[7;32;40m"
print(f"{Vd_Bk}Bora somar?\033[0m")
cardinal = 1
A = float(input("Digite o número {} de deseja somar:" .format(cardinal)))
B = float(input("Digite o número {} de deseja somar:" .format(cardinal + 1)))
t1 = A + B
cardinal += 1
R = input("Deseja somar mais um número? \n>[S/N]<")
if R == "N" or R == 'n':
    print('O resultado da sua some é:', A + B, "!")
else:
    while R == 'S' or "s":
        cardinal += 1
        V = float(input("Digite o número {} de deseja somar:".format(cardinal)))
        t1 += V
        R = input("Deseja somar mais um número? \n>[S/N]<")
        if R == "N" or R == 'n':
            print('O resultado da sua some é:', t1, "!")
            break
