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
        self.botoes = [[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]] 
        
        for i in range(0, 3): 
            for j in range(0, 3): 
                self.botoes[i][j] = tk.Button(self.window) 
                self.botoes[i][j].configure(height=10, width=10, command=lambda botao=(i,j): self.botao_comando(botao))
                self.botoes[i][j].grid(row=i, column=j, sticky="nsew")
                                              
        # Labels
        self.label_indicador = tk.Label(self.window) 
        self.label_indicador.configure(width=60, height=1)
        self.label_indicador.grid(row=3, column=0, columnspan=3, sticky="w")
        
        self.cria_label("Primeira jogada: {0}".format(self.meu_jogo.jogador))
                    
    def cria_botoes(self, posicao, limpar_tabuleiro):
        texto_botao = tk.StringVar()
        texto_botao.set("")
       
        if limpar_tabuleiro == False:
            texto_botao.set(self.meu_jogo.jogador)
        
        self.botoes[posicao[0]][posicao[1]].config(textvariable = texto_botao,\
                state="disabled") 
        
        self.cria_label("Próxima Jogada: {0}".format(self.meu_jogo.proximo))

    def cria_label(self, texto): 
        label_indicador = tk.StringVar()
        label_indicador.set(texto)
        self.label_indicador.configure(textvariable = label_indicador, anchor="w")
    
    def botao_comando(self, posicao): 
        
        self.cria_botoes(posicao, False)
        self.meu_jogo.recebe_jogada(posicao)

        resultado = self.meu_jogo.verifica_ganhador()
        
        if resultado == -1: 
            pass
        elif resultado == 0:
            self.quem_venceu("O jogo empatou!")
        elif resultado == 1:
            self.quem_venceu("Vencedor: Jogador X")
        elif resultado == 2:
            self.quem_venceu("Vencedor: Jogador O")
            
    def quem_venceu(self, resultado): 
        
        self.nova_janela = tkm.askquestion("Resultado", "{0}\nDeseja começar um novo jogo?".format(resultado))        
        
        self.meu_jogo.limpa_jogadas()
        self.limpa_tela()

        if self.nova_janela == "no":
            self.window.destroy()

    def limpa_tela(self): 
        
        for i in range(0,3):
            for j in range(0,3):
                self.cria_botoes((i,j), True) 
                self.botoes[i][j].config(state="normal") 
        
        self.cria_label("Primeira Jogada: {0}".format(self.meu_jogo.jogador)) 
        

    def iniciar(self):
        self.window.mainloop()
        
        
class Final_Jogo:
    def __init__(self):
        self.Final_Jogo = tk.Tk()
        self.Final_Jogo.title("Resultado do Jogo da Velha")
        self.Final_Jogo.geometry("100x200")
       
       
app = Tabuleiro()
app.iniciar()