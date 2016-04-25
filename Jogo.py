import tkinter as tk
import numpy as np


R = 9 #Resultado
class MockJogoDaVelha:
    def __init__(self):
        self.jogador = 1
        self.matriz = np.zeros([3,3])
        self.rodada = 1
        
    def recebe_jogada(self, linha, coluna): #Recebe e registra uma jogada e alterna jogadores
        if self.jogador == 1:
            self.jogador = 2
            self.rodada += 1
            
        else:
            self.jogador = 1
    
    def verifica_ganhador(self): #Verifica se o jogo acabou, retorna 0 em caso de empate, 1 se X ganhou e 2 se Y ganhou, -1 caso contrário
        if # X ganhou
            R = 1
        elif # Y ganhoy
            R = 2
        elif self.rodada = 9 #Empate/Velha
            R = 0
        else:
            R = -1
        return R
        
    def limpa_jogadas(): #Reinicia o jogo
    
    