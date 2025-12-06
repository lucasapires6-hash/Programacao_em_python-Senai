import tkinter as tk
from tkinter import ttk

def enviar_dados():
    print("===== Dados do Cliente =====")
    print("Nome:", entry_nome.get())
    print("Idade:", entry_idade.get())
    print("E-mail:", entry_email.get())
    print("Endereço:", entry_endereco.get())
    print("Celular:", entry_celular.get())
    print("CEP:", entry_cep.get())
    print("Cidade:", entry_cidade.get())
    print("Cursos:", entry_cursos.get())
    print("============================\n")

# Janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro de Clientes")
janela.geometry("1700x750")

# Título
titulo = tk.Label(janela, text="Formulário de Cadastro de Clientes", font=("Arial", 22, "bold"))
titulo.pack(pady=20)

# Frame para organizar os campos
frame = tk.Frame(janela)
frame.pack(pady=20)

# Nome
tk.Label(frame, text="Nome:", font=("Arial", 14)).grid(row=0, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(frame, width=40, font=("Arial", 14))
entry_nome.grid(row=0, column=1, pady=5)

# Idade
tk.Label(frame, text="Idade:", font=("Arial", 14)).grid(row=1, column=0, sticky="w", pady=5)
entry_idade = tk.Entry(frame, width=40, font=("Arial", 14))
entry_idade.grid(row=1, column=1, pady=5)

# E-mail
tk.Label(frame, text="E-mail:", font=("Arial", 14)).grid(row=2, column=0, sticky="w", pady=5)
entry_email = tk.Entry(frame, width=40, font=("Arial", 14))
entry_email.grid(row=2, column=1, pady=5)

# Endereço
tk.Label(frame, text="Endereço:", font=("Arial", 14)).grid(row=3, column=0, sticky="w", pady=5)
entry_endereco = tk.Entry(frame, width=40, font=("Arial", 14))
entry_endereco.grid(row=3, column=1, pady=5)

# Celular
tk.Label(frame, text="Celular:", font=("Arial", 14)).grid(row=4, column=0, sticky="w", pady=5)
entry_celular = tk.Entry(frame, width=40, font=("Arial", 14))
entry_celular.grid(row=4, column=1, pady=5)

# CEP
tk.Label(frame, text="CEP:", font=("Arial", 14)).grid(row=5, column=0, sticky="w", pady=5)
entry_cep = tk.Entry(frame, width=40, font=("Arial", 14))
entry_cep.grid(row=5, column=1, pady=5)

# Cidade
tk.Label(frame, text="Cidade:", font=("Arial", 14)).grid(row=6, column=0, sticky="w", pady=5)
entry_cidade = tk.Entry(frame, width=40, font=("Arial", 14))
entry_cidade.grid(row=6, column=1, pady=5)

# Cursos
tk.Label(frame, text="Cursos:", font=("Arial", 14)).grid(row=7, column=0, sticky="w", pady=5)
entry_cursos = tk.Entry(frame, width=40, font=("Arial", 14))
entry_cursos.grid(row=7, column=1, pady=5)

# Botão Enviar
botao_enviar = tk.Button(janela, text="Enviar", font=("Arial", 16), bg="green", fg="white", command=enviar_dados)
botao_enviar.pack(pady=30)

# Rodar janela
janela.mainloop()
