#CRIANDO UM DATAFRAME DE PANDAS ATRAVES DE UM WORKBOOK DE OPENPYXL


import pandas as pd
from openpyxl import Workbook
import openpyxl as py
from time import sleep
wb = Workbook()
cliente = wb.active
cliente.title = "Clientes"
adm = wb.create_sheet("Administradores")
cliente["A1"] = "Nome"
cliente["B1"] = "Data de nascimento"
cliente["C1"] = "Email"
cliente["D1"] = "CPF"
cliente["E1"] = "Senha"
adm["A1"] = "Nome"
adm["B1"] = "Data de nascimento"
adm["C1"] = "Email"
adm["D1"] = "CPF"
adm["E1"] = "Senha"
sleep(0.5)
df = wb.get_sheet_by_name("Administradores")
df = pd.DataFrame(df)
print(df)