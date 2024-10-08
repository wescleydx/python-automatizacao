from cProfile import label
from cgitb import text
from sqlite3 import Row
from struct import pack
from tkinter import font
from tkinter.tix import COLUMN
from turtle import heading, width
from tkinter import *
from func_first import proc_one
from func_second import proc_second
from func_third import proc_third
from func_fourth import proc_fourth
from func_fifth import proc_fifth
from func_sixth import proc_sixth
from func_seventh import proc_seventh
from func_eighth import proc_eighth
from func_ninth import proc_ninth
from func_tenth import proc_tenth

"""Esse é um projeto inicial de automatização de processos repetitivos em um setor operacional de recebimento de notas.
O usuário recebe A NF e visualiza, acessa o sistema e descreve cada número de pedido, caso seja um pedido com 14 requisições, ele fará
esse processo repetidamente 14 vezez, inserindo a numeração das NF e executando no sistema.
"""
## Nesse projeto eu pude começar os estudos na línguagem python e aos poucos melhorar o código e criar derivados.

## Janela da interface
janela = Tk()
janela.title("WM [BETA] - Desenvolvido por Wescley")
janela.geometry("430x38")
janela.resizable(False,False) 
janela['bg']= "#000000"

## ------------------------ Número de repetições ------------------------ ##  01    FF 45 00    FF A5 00
texto_orientacao=Label(janela, text="Escolha o número de repetições",bg="#FFFF00", foreground="#000000")
texto_orientacao.grid(column=10, row=1,  padx=7, pady=7)

## ------------------------ Botões ------------------------## 02

# Ao clicar na opção desejada, a função correta será chamada para realização da tarefa #

texto_orientacao= Label(janela, text="1",bg="#FFFF00", foreground="#000000")
texto_orientacao.grid(column=0, row=1, padx=3, pady=3)
botao= Button(janela, text="1", command=proc_one, bg="#FFFF00", foreground="#000000")
botao.grid(column=0, row=1, padx=3, pady=3)

texto_orientacao= Label(janela, text="2")
texto_orientacao.grid(column=1, row=1, padx=3, pady=3)
botao= Button(janela, text="2", command=proc_second, bg="#FFFF00", foreground="#000000")
botao.grid(column=1, row=1, padx=3, pady=3)

texto_orientacao= Label(janela, text="3")
texto_orientacao.grid(column=2, row=1, padx=3, pady=3)
botao= Button(janela, text="3", command=proc_third, bg="#FFFF00", foreground="#000000")
botao.grid(column=2, row=1, padx=3, pady=3)

texto_orientacao= Label(janela, text="4")
texto_orientacao.grid(column=3, row=1, padx=3, pady=3)
botao= Button(janela, text="4", command=proc_fourth, bg="#FFFF00", foreground="#000000")
botao.grid(column=3, row=1, padx=3, pady=3)

texto_orientacao= Label(janela, text="5")
texto_orientacao.grid(column=4, row=1, padx=3, pady=3)
botao= Button(janela, text="5", command=proc_fifth, bg="#FFFF00", foreground="#000000")
botao.grid(column=4, row=1, padx=3, pady=3)

texto_orientacao= Label(janela, text="6")
texto_orientacao.grid(column=5, row=1, padx=3, pady=3)
botao= Button(janela, text="6", command=proc_sixth, bg="#FFFF00", foreground="#000000")
botao.grid(column=5, row=1, padx=3, pady=3)

texto_orientacao= Label(janela, text="7")
texto_orientacao.grid(column=6, row=1, padx=3, pady=3)
botao= Button(janela, text="7", command=proc_seventh, bg="#FFFF00", foreground="#000000")
botao.grid(column=6, row=1, padx=3, pady=3)

texto_orientacao= Label(janela, text="8")
texto_orientacao.grid(column=7, row=1, padx=3, pady=3)
botao= Button(janela, text="8", command=proc_eighth, bg="#FFFF00", foreground="#000000")
botao.grid(column=7, row=1, padx=3, pady=3)

texto_orientacao= Label(janela, text="9")
texto_orientacao.grid(column=8, row=1, padx=3, pady=3)
botao= Button(janela, text="9", command=proc_ninth, bg="#FFFF00", foreground="#000000")
botao.grid(column=8, row=1, padx=3, pady=3)

texto_orientacao= Label(janela, text="10")
texto_orientacao.grid(column=9, row=1, padx=3, pady=3)
botao= Button(janela, text="10", command=proc_tenth, bg="#FFFF00", foreground="#000000")
botao.grid(column=9, row=1, padx=3, pady=3)

janela.mainloop()
