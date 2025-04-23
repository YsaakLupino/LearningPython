import tkinter as tk

def mostrar_resultado():
    opcao_selecionada = valor_selecionado.get()
    resultado_label.config(text=f"Você selecionou: {opcao_selecionada}")

root = tk.Tk()
root.title("Tela com Menu Suspenso")

# Lista de opções
opcoes = ["Opção 1", "Opção 2", "Opção 3"]

# Variável de controle para armazenar a opção selecionada
valor_selecionado = tk.StringVar(root)
valor_selecionado.set(opcoes[0])  # Define o valor padrão

# Cria o menu suspenso
menu_suspenso = tk.OptionMenu(root, valor_selecionado, *opcoes)
menu_suspenso.pack(pady=10)

# Botão para mostrar o resultado
botao = tk.Button(root, text="Mostrar Resultado", command=mostrar_resultado)
botao.pack(pady=10)

# Rótulo para exibir o resultado
resultado_label = tk.Label(root, text="Você selecionou: ")
resultado_label.pack()

root.mainloop()