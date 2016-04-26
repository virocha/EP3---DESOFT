# -*- coding: utf-8 -*-
"""
Insper - Engenharia 1B
Design de Software
EP3: Jogo da Velha

Vitória Rocha e Isabella Oliveira
"""

import tkinter as tk
import tkinter.messagebox as tkm
from Jogo import Jogo

class Tabuleiro:
    def __init__(self):
        self.meu_jogo = Jogo() 

        # Janela principal
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("450x520")
        
        for i in range(0, 3):
            self.window.rowconfigure(i, minsize=150)
            self.window.columnconfigure(i, minsize=150)
        
        self.window.rowconfigure(3, minsize=40)

        # Botões
        global botoes 
        botoes = [[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]] 
        
        for i in range(0, 3): 
            for j in range(0, 3): 
                botoes[i][j] = tk.Button(self.window) 
                botoes[i][j].configure(height=10, width=10, command=lambda botao=(i,j): self.botao_comando(botao))
                botoes[i][j].grid(row=i, column=j, sticky="nsew")
        
        #  Labels
        global label_1 
        
        label_1 = tk.Label(self.window) 
        label_1.configure(width=60, height=1)
        label_1.grid(row=3, column=0, columnspan=3, sticky="w")
        
        self.cria_label("Primeira Jogada: {0}".format(self.meu_jogo.jogada))
    
    def cria_botoes(self, posicao, limpar_tabuleiro):
        texto_botao = tk.StringVar()
        
        if limpar_tabuleiro == False:
            texto_botao.set(self.meu_jogo.jogada) 
        else:
            texto_botao.set("") 

        global botoes
        botoes[posicao[0]][posicao[1]].config(textvariable = texto_botao,\
                state="disabled") 
        
        self.cria_label("Próxima Jogada: {0}".format(self.meu_jogo.proxima_jogada))

    def cria_label(self, display): 
        texto_label = tk.StringVar()
        texto_label.set(display)
        
        global label_1
        label_1.configure(textvariable = texto_label, anchor="w")
    
    def botao_comando(self, posicao): 
        
        self.cria_botoes(posicao, False)
        self.meu_jogo.recebe_jogada(posicao)

        resultado = self.meu_jogo.verifica_ganhador()

    def limpa_tela(self): 
        for i in range(0,3):
            for j in range(0,3):
                self.cria_botoes((i,j), True) 
                botoes[i][j].config(state="normal") 
        
        self.cria_label("Primeira Jogada: {0}".format(self.meu_jogo.jogada)) 

    def iniciar(self):
        self.window.mainloop()

       
app = Tabuleiro()
app.iniciar()