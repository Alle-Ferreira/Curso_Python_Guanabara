'''Pacotes Nativos Python: pacote gráfico

4. tkinter
Usado para desenvolver interfaces gráficas.'''

# Sintaxe 1
import tkinter as tk
from tkinter import messagebox

def somar_numeros():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        messagebox.showinfo("Resultado", f"A soma dos números é: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números válidos.")

janela = tk.Tk()
janela.title("Calculadora de Soma")

label_num1 = tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_somar = tk.Button(janela, text="Somar", command=somar_numeros)
botao_somar.grid(row=2, columnspan=2, padx=10, pady=5)

janela.mainloop()


'''
4.1. ttk (Themed Tkinter Widgets) – mais moderno dentro do próprio tkinter
O ttk já faz parte do tkinter desde o Python 3.1 e traz widgets com visual mais moderno, temas e estilos prontos. Ele não substitui completamente o tkinter, mas melhora a aparência e oferece maior controle visual.'''

# Exemplo 1: 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def somar():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        resultado.set(f"{n1 + n2}")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números.")

janela = tk.Tk()
janela.title("Calculadora com TTK")

# Entrada e layout
ttk.Label(janela, text="Número 1:").grid(row=0, column=0, padx=10, pady=5)
entry1 = ttk.Entry(janela)
entry1.grid(row=0, column=1)

ttk.Label(janela, text="Número 2:").grid(row=1, column=0, padx=10, pady=5)
entry2 = ttk.Entry(janela)
entry2.grid(row=1, column=1)

ttk.Button(janela, text="Somar", command=somar).grid(row=2, column=0, columnspan=2, pady=10)

resultado = tk.StringVar()
ttk.Label(janela, textvariable=resultado).grid(row=3, column=0, columnspan=2)

janela.mainloop()


# Exemplo 2:

import tkinter as tk
from tkinter import messagebox
 
def comp_numeros():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num1 > num2 :
       messagebox.showinfo("Resultado", f"O numero {num1} é maior que {num2}")
    elif num1 == num2 :
       messagebox.showinfo("Resultado", f"O numero {num1} é  igual a {num2}")
    else:
       messagebox.showinfo("Resultado", f"O numero {num1} é menor que {num2}")

# Criando a janela
janela=tk.Tk()
janela.title("Comparando Numeros")

# Criando os widgets
label_num1=tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1=tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2=tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2=tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_comp=tk.Button(janela, text="Comparar", command=comp_numeros)
botao_comp.grid(row=2, columnspan=2, padx=10, pady=5)

# Rodando o loop principal
janela.mainloop()