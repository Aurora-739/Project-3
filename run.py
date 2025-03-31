from tabulate import tabulate
import random
import sys


def game():
    gameboard = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    def printGameboard():
        headers = ["Column 0", "Column 1", "Column 2"]
        colalign = ["center", "center", "center"]
        print(tabulate(gameboard, headers=headers, tablefmt="rounded_grid", colalign=colalign))

    def endgame():
        """
        ends the game
        """
        playagain = input(f"Would you like to play again?(y/n)\n").strip().lower()
        if playagain == "y":
            gameboard = [
                ["", "", ""],
                ["", "", ""],
                ["", "", ""]
            ]
            game()
        elif playagain != "y" and playagain != "n":
            while playagain != "y" and playagain != "n":
                playagain = input(f"Would you like to play again?(y/n)\n").strip().lower()
        else:
            print("Thank you for playing!")
            sys.exit()

    def playersChoice():
        # player = input("\nPlayer, are you X or O?:\n").strip().upper()
        player = ""
        while player != "X" and player != "O":
            player = input("\nPlayer, are you X or O?:\n").strip().upper()
            return player
    player = playersChoice()

    while True:
        """
        to continue the game until there is a Win or a loss
        """

        def check_Won():
            """
            looks at the row to see if the player / computer has 3 in a row
            """
            win = False
            for row in range(3):
                if gameboard[row][0] == gameboard[row][1] == gameboard[row][2] == player:
                    win = True
                    break
            for col in range(3):
                if gameboard[0][col] == gameboard[1][col] == gameboard[2][col] == player:
                    win = True
                    break
            if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] == player:
                """
                    Checks diagonal (top left to bot. right)
                    """
                win = True
            if gameboard[0][2] == gameboard[1][1] == gameboard[2][0] == player:
                """
                Checks diagonal (top right to bot. left)
                """
                win = True

            if win is True:
                print("You Won")
                printGameboard()
                endgame()
                return True
            return False

        def checkDraw():
            for row in gameboard:
                if "" in row:
                    return False
            print("You drew!")
            return False

        def playerMove(player):
            """
            where the player decides where to put their x / o
            """

            printGameboard()

            while True:
                try:
                    row_index = int(input("Choose your row between 0 & 2:"))
                    column_index = int(input("Choose your column between 0 & 2:"))
                    cell_value = gameboard[row_index][column_index]

                    if cell_value == "":
                        gameboard[row_index][column_index] = player
                        break
                    else:
                        print("Cell already taken, try again.")
                except (ValueError, IndexError):
                    print("Invalid input, please try again")

        def computer():
            """
            The computer's Turn
            """
            if player == "X":
                computersChoice = "O"
            else:
                computersChoice = "X"

            while True:
                try:
                    row_index = random.randint(0, 2)
                    column_index = random.randint(0, 2)
                    cell_value = gameboard[row_index][column_index]

                    if cell_value == "":
                        print("Computer's Turn...")
                        gameboard[row_index][column_index] = computersChoice
                        print(f"Computer plays: row: {row_index} & column: {column_index}")
                        break
                except (ValueError, IndexError):
                    pass

        def check_Comp_Won(computersChoice):
            if player == "X":
                computersChoice = "O"
            else:
                computersChoice = "X"
            """
            looks at the row to see if the computer has 3 in a row
            """
            win = False
            for row in range(3):
                if gameboard[row][0] == gameboard[row][1] == gameboard[row][2] == computersChoice:
                    win = True
            for col in range(3):
                if gameboard[0][col] == gameboard[1][col] == gameboard[2][col] == computersChoice:
                    win = True
                if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] == computersChoice:
                    """
                        Checks diagonal (top left to bot. right)
                        """
                    win = True
                if gameboard[0][2] == gameboard[1][1] == gameboard[2][0] == computersChoice:
                    """
                    Checks diagonal (top right to bot. left)
                    """
                    win = True

            if win is True:
                print("Computer Wins")
                printGameboard()
                endgame()
                return True
            return False

        def main():
            while True:
                # Player's turn
                playerMove(player)
                # check if player has won
                if check_Won():
                    break
                # check for draw
                if checkDraw():
                    break
                # computer's turn
                computersChoice = computer()
                # check if computer has won
                if check_Comp_Won(computersChoice):
                    break
                # check for draw
                if checkDraw():
                    break
        main()
game()
