from tkinter import *
# criando a janela principal
janela_principal = Tk()
#mudando seu titulo
janela_principal.title("Calculadora de Rd3")

#lista de opçaoes para o DropButton
opcoes = ["Regra de tres diretamente proporcional", "Regra de três inversamente proporcional"]

#Criando variável de armazenamento para o DropButton
regra_selecionada = StringVar(janela_principal)
regra_selecionada.set(opcoes[0]) #valor padrao do DropButton

#criando caixas para receber input

valor_a = Entry(janela_principal)

valor_b = Entry(janela_principal)

valor_c = Entry(janela_principal)

#criando textos para mostrar o que está para o QUE

a_para_b = Label(janela_principal, text="Está para ------->")
c_para_x = Label(janela_principal, text="Está para ------->")

assim_como = Label(janela_principal, text="_________Assim como_________")

#Criando texto de titulos para as entradas

a = Label(janela_principal, text="Valor 1")
b = Label(janela_principal, text="Valor 2")
c = Label(janela_principal, text="Valor 3")
d = Label(janela_principal, text="Valor 4")
x = Label(janela_principal, text="X")
resultado = Label(janela_principal, text="Resultado:")

#Criando botao para mostrar resultado

botao_resultado = Button(janela_principal, text="Gerar resultado")

#Criando DropButton de decisao 

selecionando = OptionMenu(janela_principal, regra_selecionada, *opcoes)

#posicionando interface

selecionando.grid(column=1, row=3)
a.grid(column=0,row=0)
valor_a.grid(column=1, row=0)
a_para_b.grid(column=2, row=0)
b.grid(column=3, row=0)
valor_b.grid(column=4,row=0)
assim_como.grid(column=3,row=1)
c.grid(column=0,row=2)
valor_c.grid(column=1,row=2)
c_para_x.grid(column=2, row=2)
d.grid(column=3,row=2)
x.grid(column=4,row=2)
botao_resultado.grid(column=3,row=3)
resultado.grid(column=2, row=4)













































janela_principal.mainloop()