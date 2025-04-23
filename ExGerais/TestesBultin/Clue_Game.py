# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

from time import sleep

pintar = "\033[1;30;41m"
pintar2 = "\033[1;33;40m"
pintar3 = "\033[1;33m"
pintar4 = "\033[1;31m"
pintar5 = "\033[1;30;43m"
pintar6 = "\033[1;42;30m"
pintar7 = "\033[1;32m"

respostas = []

resposta_telefonou = str(input(f"{pintar4}Você telefonou para a vítima? ")).lower()
while True:
    if resposta_telefonou[0] == "s":
        resposta_telefonou = True
        respostas.append(resposta_telefonou)
        break
    elif resposta_telefonou[0] == "n":
        resposta_telefonou = False
        respostas.append(resposta_telefonou)
        break
    else:
        print(f"{pintar}Resposta inválida!!\033[0m\n{pintar}Por favor insira sim ou não\033[0m")
        resposta_telefonou = str(input(f"{pintar4}Você telefonou para a vítima? ")).lower()

Resposta_presenciou = str(input(f"{pintar4}Você presenciou o crime? "))
while True:
    if Resposta_presenciou[0] == "s":
        Resposta_presenciou = True
        respostas.append(Resposta_presenciou)
        break
    elif Resposta_presenciou[0] == "n":
        Resposta_presenciou = False
        respostas.append(Resposta_presenciou)
        break
    else:
        print(f"{pintar}Resposta inválida!!\033[0m\n{pintar}Por favor insira sim ou não\033[0m")
        Resposta_presenciou = str(input(f"{pintar4}Você presenciou o crime? "))

Resposta_morou = str(input(f"{pintar4}Você mora perto do local do crime? ")).lower()
while True:
    if Resposta_morou[0] == "s":
        Resposta_morou = True
        respostas.append(Resposta_morou)
        break
    elif Resposta_morou[0] == "n":
        Resposta_morou = False
        respostas.append(Resposta_morou)
        break
    else:
        print(f"{pintar}Resposta inválida!!\033[0m\n{pintar}Por favor insira sim ou não\033[0m")
        Resposta_morou = str(input(f"{pintar4}Você mora perto do local do crime? ")).lower()


Resposta_trabalhou = str(input(f"{pintar4}Você tinha um álibi no momento do crime? ")).lower()
while True:
    if Resposta_trabalhou[0] == "s":
        Resposta_trabalhou = True
        respostas.append(Resposta_trabalhou)
        break

    elif Resposta_trabalhou[0] == "n":
        Resposta_trabalhou = False
        respostas.append(Resposta_trabalhou)
        break
    else:
        print(f"{pintar}Resposta inválida!!\033[0m\n{pintar}Por favor insira sim ou não\033[0m")
        Resposta_trabalhou = str(input(f"{pintar4}Você tinha um álibi no momento do crime? ")).lower()

Resposta_deveu = str(input(f"{pintar4}Devia para a vítima? ")).lower()
while True:
    if Resposta_deveu[0] == "s":
        Resposta_deveu = True
        respostas.append(Resposta_deveu)
        break
    elif Resposta_deveu[0] == "n":
        Resposta_deveu = False
        respostas.append(Resposta_deveu)
        break
    else:
        print(f"{pintar}Resposta inválida!!\033[0m\n{pintar}Por favor insira sim ou não\033[0m")
        Resposta_deveu = str(input(f"{pintar4}Devia para a vítima? ")).lower()

print(f'{pintar2}Um momento, estamos calculando o veredito\033[0m')
sleep(0.5)
print(f"{pintar3}Carregando.")
sleep(0.2)
print(f"{pintar3}Carregando..")
sleep(0.75)
print(f"{pintar3}Carregando...")
sleep(1)
print(f"{pintar3}Carregando....")
sleep(0.35)

verdadeiro = respostas.count(True)

if verdadeiro <= 2:
    status = "Inocente"
elif 2 < verdadeiro <= 4:
    status = "Cúmplice"
else:
    status = "Assassino"


print(f"{pintar3}você respondou com sim à \033[0m{verdadeiro}{pintar3} perguntas e foi considerado:\033[0m")


if status == "Assassino":
    p = "Você está preso!"
    print(f"{pintar4}{status:-^55}\033[0m")
    print(f"{pintar}{p:^55}\033[0m")
if status == "Cúmplice":
    p = "Fique atento!"
    print(f"{pintar3}{status:-^55}\033[0m")
    print(f"{pintar5}{p:^55}\033[0m")
if status == "Inocente":
    print(f"{pintar7}{status:-^55}\033[0m")
    p = "Desculpe o incômodo!"
    print(f"{pintar6}{p:^55}\033[0m")
