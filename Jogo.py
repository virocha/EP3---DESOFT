import numpy as np

class Jogo:
    def __init__(self):
        self.limpa_jogadas()
        
    def recebe_jogada(self, linha, coluna): #Recebe e registra uma jogada e alterna jogadores
        self.matriz[linha][coluna] = self.jogador
        if self.jogador == 1:
            self.jogador = 2
            
        else:
            self.jogador = 1
            
        self.rodada += 1
    
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
        elif self.rodada == 9: #Empate/Velha
            R = 0
        else:
            R = -1
        return R
        
    def limpa_jogadas(self): #Reinicia o jogo
        self.jogador = 1
        self.matriz = np.zeros([3,3])
        self.rodada = 1        
        
if __name__ == "__main__":
    jogo = Jogo()
    


