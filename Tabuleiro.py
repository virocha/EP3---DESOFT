import tkinter as tk

class MockJogoDaVelha:
    def __init__(self):
        self.jogador = 1
        
    def recebe_jogada(self, linha, coluna):
        pass
    
    def verifica_ganhador(self):
        return -1

class Tabuleiro:
    def __init__(self):
        
        self.jogo = MockJogoDaVelha()
        
        self.window = tk.Tk()
        self.window.geometry("300x300+100+100")
        self.window.rowconfigure(0, minsize = 100)
        self.window.rowconfigure(1, minsize = 100)
        self.window.rowconfigure(2, minsize = 100)
        self.window.rowconfigure(3, minsize = 50)
        self.window.columnconfigure(0, minsize = 100)
        self.window.columnconfigure(1, minsize = 100)
        self.window.columnconfigure(2, minsize = 100)
        
        self.chama_jogador = tk.Label(self.window)
        self.chama_jogador.configure(text = "Jogador 1: X")
        self.chama_jogador.grid(row = 3, column = 0, columnspan = 3, sticky = "nsew")
               
        self.botao1 = tk.Button(self.window)
        self.botao1.grid(row = 1, column = 0, sticky  = "nsew")
        self.botao2 = tk.Button(self.window)
        self.botao2.grid(row = 1, column = 1, sticky  = "nsew")
        self.botao3 = tk.Button(self.window)
        self.botao3.grid(row = 1, column = 2, sticky  = "nsew")
        self.botao4 = tk.Button(self.window)
        self.botao4.grid(row = 2, column = 0, sticky  = "nsew")
        self.botao5 = tk.Button(self.window)
        self.botao5.grid(row = 2, column = 1, sticky  = "nsew")
        self.botao6 = tk.Button(self.window)
        self.botao6.grid(row = 2, column = 2, sticky  = "nsew")
        self.botao7 = tk.Button(self.window)
        self.botao7.grid(row = 3, column = 0, sticky  = "nsew")
        self.botao8 = tk.Button(self.window)
        self.botao8.grid(row = 3, column = 1, sticky  = "nsew")
        self.botao9 = tk.Button(self.window)
        self.botao9.grid(row = 3, column = 2, sticky  = "nsew")
        
        
       
app = Tabuleiro()
app.iniciar()