from time import sleep
import pandas as pd
import sys
import subprocess
import pygetwindow as gw

despintar = "\033[0m"
pintar_principal = "\033[1;31;40m"
pintar_perguntas = "\033[1;37;41m" # Negrito, letra branca, fundo vermelho

print(f"{pintar_principal}Bem vindo ao programa de reajustes, por favor, insira o nome e salário dos funcionários conforme o programa pede{despintar}")

sleep(0.5)
print(".")
sleep(0.5)
print("..")
sleep(0.5)
print("...")
sleep(0.5)

nomes = []
salarios = []

def inserir_dados():
    while True:
        try:
            nome = str(input(f"{pintar_perguntas}Por favor, insira o nome do funcionário:{despintar} "))
            nomes.append(nome)
            break
        except Exception:
            print("Voce precisa digitar um nome válido")

    while True:
        try:
            salario = float(input(f"{pintar_perguntas}Por favor, insira o salário do funcionário:{despintar} "))
            salarios.append(salario)
            break
        except Exception:
            print("Voce precisa digitar um número válido")

def renovar_ciclo():
   breake = str(input("Deseja calcular o reajuste de mais algum funcionário? \n[S/N]: ")).lower()
   if breake[0] == "s":
       inserir_dados()
       renovar_ciclo()

def main():
    inserir_dados()
    renovar_ciclo()

main()

tabela_ajustes = pd.DataFrame({"Nome": nomes, "Salário": salarios})

salario_reajustado = []

for s in salarios:
    if s <= 280:
        ajuste = (s*0.2)+s
        salario_reajustado.append(ajuste)
    elif 280 < s <= 700:
        ajuste = (s*0.15)+s
        salario_reajustado.append(ajuste)
    elif 700 < s <= 1500:
        ajuste = (s*0.1)+s
        salario_reajustado.append(ajuste)
    else:
        ajuste = (s*0.05)+s
        salario_reajustado.append(ajuste)

reajuste = []

for s in salarios:
    if s <= 280:
        ajuste = (s*0.2)
        reajuste.append(ajuste)
    elif 280 < s <= 700:
        ajuste = (s*0.15)
        reajuste.append(ajuste)
    elif 700 < s <= 1500:
        ajuste = (s*0.1)
        reajuste.append(ajuste)
    else:
        ajuste = (s*0.05)
        reajuste.append(ajuste)

porcentagem_de_ajuste = []

for s in salarios:
    if s <= 280:
        pcntg = "20%"
        porcentagem_de_ajuste.append(pcntg)
    elif 280 < s <= 700:
        pcntg = "15%"
        porcentagem_de_ajuste.append(pcntg)
    elif 700 < s <= 1500:
        pcntg = "10%"
        porcentagem_de_ajuste.append(pcntg)
    else:
        pcntg = "5%"
        porcentagem_de_ajuste.append(pcntg)

tabela_ajustes = tabela_ajustes.assign(**{
    'Novo Salário': salario_reajustado,
    'Quantidade Reajustada': reajuste,
    'Porcentagem Reajustada': porcentagem_de_ajuste
})

print(f"{pintar_principal}Segue entao a tabela com as alterçãoes salariais{despintar}")
print(tabela_ajustes)

export = str(input(f"{pintar_principal}Deseja exportar as alterações para um documento do excel em sua área de trabalho?\n[S/N]:{despintar} ")).lower()

if export[0] =="n":
    print("obrigado por ultilizar o programa, até a próxima!")
    sys.exit()
else:
    pass

nome = str(input(f"{pintar_perguntas}Com qual nome o arquivo será salvo:{despintar} "))

caminho = fr"C:\Users\YSAAK\Desktop\C# projects\{nome}.xlsx"

tabela_ajustes.to_excel(caminho, index= False)

print(f"{pintar_principal}planilha exportada com sucesso para {caminho}{despintar}")

sleep(0.5)

abrir = input(f"{pintar_perguntas}Deseja abrir a planilha exportada neste momento?[S/N]:{despintar} ").lower()
if abrir[0] == "n":
    print("obrigado por ultilizar o programa, até a próxima!")
    sys.exit()
else:
    pass

print(f"{pintar_perguntas}Abrindo a planilha exportada:{despintar} '{nome}'")

excel_windows = []

contador = 0
debug = 0
while not excel_windows:
    if debug == 0:
        subprocess.Popen(caminho, shell=True)
        debug = 1
    print(f"{pintar_principal}Carregando... {contador}{despintar}", end="\r")
    sleep(0.5)
    contador += 1
    excel_windows = gw.getWindowsWithTitle(title= f"{nome} - Excel")
   

print("Obrigado por ultilizar o programa, até a próxima!")
