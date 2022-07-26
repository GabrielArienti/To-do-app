from tkinter import *
from tkinter import ttk
from dbb import *
from tkinter import messagebox

# Cores
cor_branco = "#fafafa"
cor_preto = "#0d0d0d"
cor_amarelo = "#f2e200"
cor_vermelho = "#d10902"
cor_azul = "#010963"
cor_entry = "#ede9e8"

# Janela principal
janela = Tk()
janela.geometry("500x225")
janela.title("To-do App")
janela.configure(bg=cor_branco)
janela.resizable(width=FALSE, height=FALSE)

# Frames

frame_esquerda = Frame(janela, width=300, height=225,
                       relief=FLAT, bg=cor_branco)
frame_esquerda.grid(row=0, column=0, sticky=NSEW)

frame_direita = Frame(janela, width=200, height=250,
                      relief=FLAT, bg=cor_branco)
frame_direita.grid(row=0, column=1, sticky=NSEW)


# Frame esquerda

frame_esq_cima = Frame(frame_esquerda, width=300, height=50,
                       relief=FLAT, bg=cor_branco)
frame_esq_cima.grid(row=0, column=0, sticky=NSEW)

frame_esq_baixo = Frame(frame_esquerda, width=300, height=175,
                        relief=FLAT, bg=cor_branco)
frame_esq_baixo.grid(row=1, column=0, sticky=NSEW)

# Função atualizar e novo


def main(a):
    # para função "nova"
    if a == "Novo":
        for widget in frame_esq_baixo.winfo_children():
            widget.destroy()

        def adicionar():
            tarefa_entry = entry.get()
            inserir([tarefa_entry])
            mostrar()
            messagebox.showinfo('Concluído', "Tarefa adicionada com sucesso.")

        lb = Label(frame_esq_baixo, text="Insira a nova tarefa", width=20,
                   height=5, relief=FLAT, anchor=CENTER, font="Courier", bg=cor_branco, fg=cor_preto)
        lb.grid(row=0, column=0, sticky=NSEW)

        entry = Entry(frame_esq_baixo, width=49, bg=cor_entry)
        entry.grid(row=1, column=0, sticky=NSEW)

        b_adicionar = Button(frame_esq_baixo, command=adicionar, text="Adicionar", width=10, height=1,
                             bg=cor_azul, pady=2, fg=cor_branco, font="15", anchor=CENTER, relief=FLAT, overrelief=RAISED)
        b_adicionar.grid(row=2, column=0, sticky=NSEW, rowspan=1, pady=1)

    # para função atualizar
    if a == "Atualizar":
        for widget in frame_esq_baixo.winfo_children():
            widget.destroy()

        def on():

            lb = Label(frame_esq_baixo, text="Atualizar tarefa", width=20,
                       height=5, relief=FLAT, anchor=CENTER, font="Courier", bg=cor_branco, fg=cor_preto)
            lb.grid(row=0, column=0, sticky=NSEW)

            entry = Entry(frame_esq_baixo, width=49, bg=cor_entry)
            entry.grid(row=1, column=0, sticky=NSEW)

            valor_selecionado = listbox.curselection()[0]
            palavra = listbox.get(valor_selecionado)
            entry.insert(0, palavra)
            tarefas = selecionar()

            def alterar():
                for item in tarefas:
                    if palavra == item[1]:
                        nova = [entry.get(), item[0]]
                        atualizar(nova)
                        entry.delete(0, END)
                mostrar()
                messagebox.showinfo(
                    'Concluído', "Tarefa atualizada com sucesso.")
            b_alterar = Button(frame_esq_baixo, text="Atualizar", width=10, height=1,
                               bg=cor_azul, pady=2, fg=cor_branco, font="15", anchor=CENTER, relief=FLAT, overrelief=RAISED, command=alterar)
            b_alterar.grid(row=2, column=0, sticky=NSEW, rowspan=1, pady=1)

        on()


# Função remover
def bremover():
    valor_selecionado = listbox.curselection()[0]
    palavra = listbox.get(valor_selecionado)

    tarefas = selecionar()

    for item in tarefas:
        if palavra == item[1]:
            deletar([item[0]])
    mostrar()
    messagebox.showinfo('Concluído', "Tarefa removida com sucesso.")


# Botão
botao_novo = Button(frame_esq_cima, command=lambda: main("Novo"), text="Novo", width=10, height=1,
                    bg=cor_azul, fg=cor_branco, font="15", anchor=CENTER, relief=FLAT, overrelief=RAISED)
botao_novo.grid(row=0, column=0, sticky=NSEW, pady=1)

botao_remover = Button(frame_esq_cima, text="Remover", width=10, height=1,
                       bg=cor_vermelho, fg=cor_branco, font="15", anchor=CENTER, relief=FLAT, overrelief=RAISED, command=bremover)
botao_remover.grid(row=0, column=1, sticky=NSEW, pady=1)

botao_atualizar = Button(frame_esq_cima, command=lambda: main("Atualizar"), text="Atualizar", width=10, height=1,
                         bg=cor_amarelo, fg=cor_preto, font="15", anchor=CENTER, relief=FLAT, overrelief=RAISED)
botao_atualizar.grid(row=0, column=2, sticky=NSEW, pady=1)

# Frame Direita

label = Label(frame_direita, text="Lista de Tarefas", width=37,
              height=1, pady=7, padx=10, relief=FLAT, anchor=W, font="Courier 14 italic", bg=cor_branco, fg=cor_preto)
label.grid(row=0, column=0, sticky=NSEW, pady=1)

listbox = Listbox(frame_direita, font="Courier 10", width=1, bg=cor_branco)
listbox.grid(row=1, column=0, sticky=NSEW, pady=5)


# Tarefas

def mostrar():
    listbox.delete(0, END)
    tarefas = selecionar()
    for item in tarefas:
        listbox.insert(END, item[1])


mostrar()

janela.mainloop()
