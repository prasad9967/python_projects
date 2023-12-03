import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.curr_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttonsGrid = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=15, height=5,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttonsGrid.append(row)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.curr_player
            self.buttonsGrid[row][col].config(text=self.curr_player)
            if self.check_winner(self.curr_player):
                messagebox.showinfo("Game Over", f"Player {self.curr_player} wins!")
                self.window.quit()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
            else:
                self.curr_player = "O" if self.curr_player == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[2][0] == self.board[1][1] == self.board[0][2] == player:
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    while True:
        game = TicTacToe()
        game.run()
        n = input("Do you want to continue y/n : ")
        if n == 'y':
            continue
        else:
            break
