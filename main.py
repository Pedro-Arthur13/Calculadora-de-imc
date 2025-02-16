"""
 Autores: Pedro Arthur, Emanuel Rodrigues, Miguel Sthevão
 Documentação de Referência utilizada: https://tkdocs.com/
 OBS.: Optei por não utilizar a https://docs.python.org/3/library/tk.html, pois aparentemente está desatualizada
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename # para poder abrir um arquivo
from tkinter.filedialog import asksaveasfilename # para poder salvar um arquivo

# classe para excecao da altura e peso
class NegativeValueError(Exception): # semelhante a "class ValueError(Exception): ..."
    """Classe de excecao personalizada para valores negativos ou zero."""
    pass

# formata o nome para quando salvar, o nome do arquivo ficar certinho
def formatar_nome(nome:str) -> str:
    return nome.replace(" ","_")

# calcula imc
def calcular_imc():
    try:
        # converte peso e altura pra float
        peso_valor = float(peso.get())
        altura_valor = float(altura.get())

        # verifica se o peso eh positivo
        if peso_valor <= 0:
            raise NegativeValueError("O valor do peso deve ser maior que zero")
        
        # verifica se a altura eh positivp
        if altura_valor <= 0:
            raise NegativeValueError("O valor da altura deve ser maior que zero")

        # calcula o IMC
        resultado = peso_valor / (altura_valor ** 2)
        
        # seta o StringVar com o resultado formatado com 2 casas decimais
        imc.set(f"{resultado:.2f}")
        mensagemImc.set(f"Seu Imc é de {resultado:.2f}")
        # salva as informações no arquivo
        conteudo = f"Nome: {nome.get()}\nPeso: {peso.get()}\nAltura: {altura.get()}\nIMC: {imc.get()}"
        with open(f"{formatar_nome(nome.get())}_Info.txt", 'w') as arquivo1:
            arquivo1.write(conteudo)
        
    except ValueError:
        # exceçao caso a altura ou o peso não sejam numéricos
        imc.set("Erro: Peso e altura devem ser números válidos")
    except NegativeValueError as e:
        # exceçao personalizado para valores negativos ou zero
        imc.set(f"Erro: {str(e)}")


# definindo a funcao de mudar o tema
def toggle_theme():
    global tema  # garante que a variavel tema seja global
    if tema == "light":
        window.configure(bg="gray")
        style.configure("TFrame", background="gray")
        style.configure("TButton", background="gray", foreground="black")
        for widget in mainframe.winfo_children():
            if isinstance(widget, ttk.Label):
                widget.configure(background="gray")
            if isinstance(widget, ttk.Entry):
                widget.configure(style="TEntry")
        theme_button.config(text="Modo Claro")
        tema = "dark"   # atualizando a variavel tema
    else:
        window.configure(bg="white")
        style.configure("TFrame", background="white")
        style.configure("TButton", background="white", foreground="black")
        for widget in mainframe.winfo_children():
            if isinstance(widget, ttk.Label):
                widget.configure(background="white")
            if isinstance(widget, ttk.Entry):
                widget.configure(style="TEntry")
        theme_button.config(text="Modo Escuro")
        tema = "light" 
        
#window
window = tk.Tk()  # cria objeto window 
window.title("Calculadora de IMC")  # Nome da Janela
icon = tk.PhotoImage(file="icon.png")  # caminho do icone
window.iconphoto(True, icon) # setando ele para ser o icone
# o geometry(valor1xvalor2) define um tamanho inicial da window
window.geometry("400x550") # com o geometry posso redimensionar a window usando o mouse
window.minsize(width=370, height=420) # defino o tamanho mínimo da window

style = ttk.Style()

# tema inicial
tema = "light"  # incializa com "light"

mainframe = ttk.Frame(window,padding="10 10 12 12")
mainframe.grid(column=0,row=0)
window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)

# OBS.: O tipo de dado StringVar possui uma funcao get, que permite ser setado o valor depois de criado como por exemplo na funcao calcular_imc
peso = StringVar()
altura = StringVar()
nome = StringVar()
# imc:StringVar (tentar transformar peso e altura em int resulta em erro, pois sao StringVar e nao str)
imc = StringVar()
mensagemImc = StringVar()

# entry para o nome
ttk.Label(mainframe,text="Nome",padding=(0,15,0,10)).grid(column=2,row=1)
altura_entry = ttk.Entry(mainframe, width=15, textvariable=nome) 
altura_entry.grid(column=2, row=2) 

# entry para o peso
ttk.Label(mainframe,text="Peso",padding=(0,15,0,10)).grid(column=2,row=3)
peso_entry = ttk.Entry(mainframe, width=15, textvariable=peso)
peso_entry.grid(column=2, row=4)

# entry para a altura
ttk.Label(mainframe,text="Altura em metros(x.xx)",padding=(0,15,0,10)).grid(column=2,row=5)
altura_entry = ttk.Entry(mainframe, width=15, textvariable=altura) #  Entry = def __init__(self, master=None, widget=None, **kw):
altura_entry.grid(column=2, row=6,pady=(0,20)) 



# label para o Título
titulo_label = ttk.Label(mainframe,text="Calculadora de IMC")
titulo_label.grid(column=2, row=0,  sticky="N")
titulo_label.config(font=("Helvetica", 24, "bold"))



# button para calcular o imc 
calcular_btn = ttk.Button(mainframe, text="Calcular", padding=(15, 15, 15, 15), command=calcular_imc)
calcular_btn.grid(column=2, row=7)

# tira a borda  azul feia que fica quando clica removendo o focp
calcular_btn.bind("<FocusIn>", lambda event: calcular_btn.master.focus())

# Botão de alternância de tema
theme_button = ttk.Button(mainframe, text="Modo Escuro", command=toggle_theme)
theme_button.grid(row=12, column=2)  # Ajustado para o canto superior direito
theme_button.bind("<FocusIn>", lambda event: theme_button.master.focus()) # retira o foco do butao

# label para mostrar o resultado do imc
ttk.Label(mainframe, textvariable=mensagemImc,padding=(0, 0, 0, 15)).grid(column=2, row=9)


window.mainloop()  #loop do objeto window