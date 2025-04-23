from time import sleep
import pandas as pd
import sys

print("Bem vindo ao programa de reajustes :)\n" +
      "Por favor, insira o nome e salário dos funcionários conforme o programa pede")

from time import sleep

def carregar():
    print("Carregando",end="", flush=True)
    for n in range(3):
        sleep(0.5)
        print(".",end="", flush=True)
    sleep(0.5)
    print("\n")
carregar()
 
nomes = []
salarios = []


def inserir_dados():
    while True:
        try:
            nome = str(input("Por favor, insira o nome do funcionário"))
            nomes.append(nome)
            break
        except Exception:
            print("Voce precisa digitar um nome válido")

    while True:
        try:
            salario = float(input("Por favor, insira o salário do funcionário"))
            salarios.append(salario)
            break
        except Exception:
            print("Voce precisa digitar um número válido")


def renovar_ciclo():
    breake = str(input("Deseja calcular o reajuste de mais algum funcionário? \n[S/N]")).lower()
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
        ajuste = (s * 0.2) + s
        salario_reajustado.append(ajuste)
    elif 280 < s <= 700:
        ajuste = (s * 0.15) + s
        salario_reajustado.append(ajuste)
    elif 700 < s <= 1500:
        ajuste = (s * 0.1) + s
        salario_reajustado.append(ajuste)
    else:
        ajuste = (s * 0.05) + s
        salario_reajustado.append(ajuste)

reajuste = []

for s in salarios:
    if s <= 280:
        ajuste = (s * 0.2)
        reajuste.append(ajuste)
    elif 280 < s <= 700:
        ajuste = (s * 0.15)
        reajuste.append(ajuste)
    elif 700 < s <= 1500:
        ajuste = (s * 0.1)
        reajuste.append(ajuste)
    else:
        ajuste = (s * 0.05)
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

print("Segue entao a tabela com as alterçãoes salariais")
print(tabela_ajustes)

export = str(input("Deseja exportar as alterações para um documento do excel em sua área de trabalho?\n[S/N]")).lower()

if export[0] == "n":
    print("obrigado por ultilizar o programa, até a próxima!")
    sys.exit()
else:
    pass

nome = str(input("Com qual nome o arquivo será salvo"))

caminho = fr"E:\pinoso\Empregos\programação\Pycharm\exercicios\{nome}.xlsx"

tabela_ajustes.to_excel(caminho, index=False)

print(f"planilha exportada com sucesso para {caminho}")

sleep(0.5)

print("obrigado por ultilizar o programa, até a próxima!")
