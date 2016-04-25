import tkinter as tk
import numpy as np

Matriz = np.zeros([3,3])

print(Matriz)

class Jogo:
    def __init__(self):
        self.jogador = 1
        
    def recebe_jogada(self, linha, coluna): #Recebe e registra uma jogada e alterna jogadores
        if self.jogador == 1:
            self.jogador = 2
            
        else:
            self.jogador = 1
    
    def verifica_ganhador(self): #Verifica se o jogo acabou, retorna 0 em caso de empate, 1 se X ganhou e 2 se Y ganhou, -1 caso contrário
        return -1
        
    def limpa_jogadas(): #