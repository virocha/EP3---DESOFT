# -*- coding: utf-8 -*-
"""
Insper - Engenharia 1B
Design de Software
EP3: Jogo da Velha

Vitória Rocha e Isabella Oliveira
"""

import numpy as np

class Jogo:
    def __init__(self):
        self.jogador = "X"
        self.proximo = "O"
        self.matriz = np.zeros([3,3])
        self.resultado = 0      
        
    def recebe_jogada(self, posicao): 
        self.guarda_jogada(posicao)
        
        if self.jogador == "X":
            self.proximo = "O"
            
        elif self.jogador == "O":
            self.proximo = "X"
            
        self.resultado += 1
            
    def guarda_jogada(self, posicao):
        if self.jogador == "X":
            identificacao = 1
        
        elif self.jogador == "O":
            identificacao = 2
        
        self.matriz[posicao[0]][posicao[1]] = identificacao
        
        self.jogador = self.proximo
        
    def verifica_ganhador(self): #Verifica se o jogo acabou, retorna 0 em caso de empate, 1 se X ganhou e 2 se O ganhou, -1 caso contrário
        if  self.matriz[0][0] == self.matriz[0][1] == self.matriz[0][2] == 1 or \
            self.matriz[1][0] == self.matriz[1][1] == self.matriz[1][2] == 1 or \
            self.matriz[2][0] == self.matriz[2][1] == self.matriz[2][2] == 1 or \
            self.matriz[0][0] == self.matriz[1][0] == self.matriz[2][0] == 1 or \
            self.matriz[0][1] == self.matriz[1][1] == self.matriz[2][1] == 1 or \
            self.matriz[0][2] == self.matriz[1][2] == self.matriz[2][2] == 1 or \
            self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] == 1 or \
            self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] == 1: # X ganhou
            R = 1
        elif self.matriz[0][0] == self.matriz[0][1] == self.matriz[0][2] == 2 or \
             self.matriz[1][0] == self.matriz[1][1] == self.matriz[1][2] == 2 or \
             self.matriz[2][0] == self.matriz[2][1] == self.matriz[2][2] == 2 or \
             self.matriz[0][0] == self.matriz[1][0] == self.matriz[2][0] == 2 or \
             self.matriz[0][1] == self.matriz[1][1] == self.matriz[2][1] == 2 or \
             self.matriz[0][2] == self.matriz[1][2] == self.matriz[2][2] == 2 or \
             self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] == 2 or \
             self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] == 2: # O ganhou
            R = 2
        elif self.resultado == 9: #Empate/Velha
            R = 0
        else:
            R = -1
        return R
        
    def limpa_jogadas(self): #Reinicia o jogo e define o jogador que vai iniciar o jogo
        
        if self.resultado == "X": 
            self.jogador = "X"
            self.proximo = "O"
        
        elif self.resultado == "O":
            self.jogador = "O"
            self.proximo = "X"

        elif self.resultado == -1: 
            self.jogador = self.proximo
            if self.jogador == "X":
                self.proximo = "O"
            else:
                self.proximo = "X"
        
        self.matriz = np.zeros([3,3])
        
if __name__ == "__main__":
    jogo = Jogo()
    


