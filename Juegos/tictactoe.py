import tkinter as tk

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(True, True)

        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.player = 1
        self.create_widgets()
    
    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self, width=5, height=2, command=lambda i=i, j=j: self.play(i, j))
                button.grid(row=i, column=j)
    
    def play(self, i, j):
        if self.board[i][j] == 0:
            self.board[i][j] = self.player
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
    
    def check_winner(self):
        pass # Aqui debes implementar la logica para verificar quien gano
    

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()