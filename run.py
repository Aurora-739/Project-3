from tabulate import tabulate
import random
import sys

class GameBoard:
    """
    Tic Tac Toe board
    """
    def __init__(self):
        self.board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    def printGameboard(self):
        headers = ["Column 0", "Column 1", "Column 2"]
        colalign = ["center", "center", "center"]
        print(tabulate(self.board, headers=headers, tablefmt="rounded_grid", colalign=colalign))

    def update_cell(self, row, col, symbol):
        """
        Updates the cells on the board with the given symbol (players choice/ computers choice)
        """
        if self.board[row][col] == "":
            self.board[row][col] = symbol
            return True
        return False
    
    def check_Won(self, symbol):
            """
            looks at the row to see if the player / computer has 3 in a row
            """
            for row in range(3):
                if self.board[row][0] == self.board[row][1] == self.board[row][2] == symbol:
                    return True
            for col in range(3):
                if self.board[0][col] == self.board[1][col] == self.board[2][col] == symbol:
                    return True
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
                """
                    Checks diagonal (top left to bot. right)
                    """
                return True
            if self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
                """
                Checks diagonal (top right to bot. left)
                """
                return True
            
            return False

    def checkDraw(self):
        for row in self.board:
            if "" in row:
                return False
        print("You drew!")
        return True

class Player:
    """
    a player ("x" or "0")
    """
    def __init__(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        """
        returns the player either "x" or "o"
        """
        return self.symbol

class TicTacToeGame:
    def __init__(self):
        self.board = GameBoard()
        self.player = None
        self.computer = None
        self.curren_player = None
    
    def playersChoice(self):
        """
        sets up player as "x" or "o"
        """
        while True:
            player_symbol = input("\nPlayer, are you X or O?:\n").strip().upper()
            if player_symbol == "X" or player_symbol == "O":
                break
            else:
                print("\nPlayer, are you X or O?:\n")
        self.player = Player(player_symbol)
        self.computer = Player("O" if player_symbol == "X" else "X")

    def playerMove(self):
            """
            where the player decides where to put their x / o
            """
            self.board.printGameboard()

            while True:
                try:
                    row_index = int(input("Choose your row between 0 & 2:"))
                    column_index = int(input("Choose your column between 0 & 2:"))

                    if self.board.update_cell(row_index, column_index, self.player.get_symbol()):
                        break
                    else:
                        print("Cell already taken, try again.")
                except (ValueError, IndexError):
                    print("Invalid input, please try again")

    def computerMove(self):
            """
            The computer's Turn
            """
            self.board.printGameboard()
            while True:
                try:
                    row_index = random.randint(0, 2)
                    column_index = random.randint(0, 2)

                    if self.board.update_cell(row_index, column_index, self.computer.get_symbol()):
                        print("Computer's Turn...")
                        print(f"Computer plays: row: {row_index} & column: {column_index}")
                        break
                except (ValueError, IndexError):
                    pass                
    
    def endGame(self):
        """
        ends the game
        """
        playagain = input(f"Would you like to play again?(y/n)\n").strip().lower()
        if playagain == "y":
            main()
        elif playagain != "y" and playagain != "n":
            while playagain != "y" and playagain != "n":
                playagain = input(f"Would you like to play again?(y/n)\n").strip().lower()
        else:
            print("Thank you for playing!")
            sys.exit()

    def checkWinner(self):
        """
        checks for winner
        """
        if self.board.check_Won(self.player.get_symbol()):
            print("You Won!!!")
            self.endGame()
            return True
        if self.board.check_Won(self.computer.get_symbol()):
            print("Computer Won")
            self.endgame()
            return True
        return False
    
    

    def game(self):
        """
        Main Game Loop
        """
        GameBoard
        self.playersChoice()
        while True:
            self.playerMove()
            if self.checkWinner():
                break
            if self.board.checkDraw():
                print("You drew!")
                self.endGame()
                break
            
            #computer
            self.computerMove()
            if self.checkWinner():
                break
            if self.board.checkDraw():
                print("Your drew!")
                self.endGame()
                break

def main():
    """
    Main loop --> starts game
    """
    game = TicTacToeGame()
    game.game()

main()