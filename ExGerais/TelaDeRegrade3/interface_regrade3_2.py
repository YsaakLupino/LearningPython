import tkinter as tk

def calcular_regra_de_tres():
    try:
        valor1 = float(entry1.get())
        valor2 = float(entry2.get())
        valor3 = float(entry3.get())

        # Realize o cálculo da regra de três
        resultado = (valor3 * valor2) / valor1

        # Atualize o rótulo de resultado
        resultado_label.config(text=f"Resultado: {resultado}")

    except ValueError:
        resultado_label.config(text="Erro: Insira valores numéricos")

def centralizar_widget(widget):
    largura_tela = widget.winfo_screenwidth()
    altura_tela = widget.winfo_screenheight()

    largura_widget = widget.winfo_reqwidth()
    altura_widget = widget.winfo_reqheight()

    x = (largura_tela - largura_widget) // 2
    y = (altura_tela - altura_widget) // 2

    widget.place(x=x, y=y)

# Crie a janela principal
root = tk.Tk()
root.title("Calculadora de Regra de Três")

# Rótulos e entradas para os valores conhecidos
label1 = tk.Label(root, text="Valor 1:")
entry1 = tk.Entry(root)

label2 = tk.Label(root, text="Valor 2:")
entry2 = tk.Entry(root)

label3 = tk.Label(root, text="Valor 3:")
entry3 = tk.Entry(root)

# Rótulo para os resultados
resultado_label = tk.Label(root, text="Resultado:")

# Botão para calcular
botao_calcular = tk.Button(root, text="Calcular", command=calcular_regra_de_tres)

# Adicione os widgets à janela
label1.grid(column=0, row=0)
entry1.grid(column=1, row=0)
label2.grid(column=0, row=2)
entry2.grid(column=1, row=2)
label3.grid(column=0, row=3)
entry3.grid(column=1, row=3)
botao_calcular.grid(row=4, column=0,)
resultado_label.grid(row=5, column=0, )

# Inicie o loop principal da aplicação
root.mainloop()
