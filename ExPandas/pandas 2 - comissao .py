import pandas as pd 
import openpyxl

Dados = {"Vendedor": ["Bob", "Charles", "Silvio", "Anderson", "josé"],
         "Comissão":[222,392,654,1232,100],
         "Salário fixo": [1200,1300,1500,1600,1700]}

df = pd.DataFrame(Dados)

qtd_vendas = []

for vendedor in Dados["Vendedor"]:
    try:
        venda = input(f"Qual a quantidade de vendas para {vendedor}")
    except ValueError:
        print("deu merda viado")
        exit
    qtd_vendas.append(int(venda))

df["QTD de vendas"] = qtd_vendas

df["Comissão em vendas"] = df["QTD de vendas"] * df["Comissão"]

df["Salário total"] = df["Comissão"] * df["QTD de vendas"] + df["Salário fixo"]

caminho = r"C:\Users\YSAAK\Desktop\C# projects\planilha de vendas.xlsx"
df.to_excel(caminho, sheet_name="teste", index=False, )
print(df)
