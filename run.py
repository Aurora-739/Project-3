from tabulate import tabulate 
import random

gameboard = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

def game():

    def endgame():
        """
        ends the game
        """
        playagain = input(f"Would you like to play again?(y/n)\n").strip().lower()
        if playagain == "y":
            game()
        elif playagain != "y" and playagain !="n":
            while playagain != "y" and playagain !="n":
                    playagain = input(f"Would you like to play again?(y/n)\n").strip().lower()
        else:
            print("Thank you for playing!")
         
    def playersChoice():
            #player = input("\nPlayer, are you X or O?:\n").strip().upper()
            player = ""
            while player != "X" and player !="O":
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
            if gameboard[0][0] == gameboard[0][1] == gameboard[0][2] == player:
                """
                row 0 == player
                """
                win == True
            elif gameboard[1][0] == gameboard[1][1] == gameboard[1][2] == player:
                """
                row 1 == player
                """
                win == True
            elif gameboard[2][0] == gameboard[2][1] == gameboard[2][2] == player:
                """
                row 2 == player
                """
                win == True
            elif gameboard[0][0] == gameboard[1][0] == gameboard[2][0] == player:
                """
                column 0 == player
                """
                win == True
            elif gameboard[0][1] == gameboard[1][1] == gameboard[2][1] == player:
                """
                column 1 == player
                """
                win == True
            elif gameboard[0][2] == gameboard[1][2] == gameboard[2][2] == player:
                """
                column 2 == player
                """
                win == True
            elif gameboard[0][0] == gameboard[1][1] == gameboard[2][2] and gameboard[0][0] != "":
                    """
                    Checks diagonal (top left to bot. right)
                    """
                    win = True
            elif gameboard[0][2] == gameboard[1][1] == gameboard[2][0] and gameboard[0][0] != "":
                    """
                    Checks diagonal (top right to bot. left)
                    """
                    win = True

            if win == True:
                print("You Won")
                return True
                endgame()

                
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

            def printGameboard():
                print(tabulate(gameboard, headers =["Column 0", "Column 1", "Column 2"], tablefmt="rounded_grid", colalign=["center", "center", "center"]))

            printGameboard()

            while True:
                try:
                    row_index = int(input("Choose your row between 0 & 2:"))
                    column_index = int(input("Choose your column between 0 & 2:"))
                    cell_value = gameboard[row_index][column_index]
                    
                    if cell_value == "":
                        gameboard[row_index][column_index] = player
                        check_Won()
                        #checkDraw()
                        computer()
                        break
                    else:
                        print("Cell already taken, try again.")
                        checkDraw()
                    
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
                    print("Computer's Turn...")
                    row_index = random.randint(0,2)
                    column_index = random.randint(0,2)
                    print(f"Computer plays: row: {row_index} & column: {column_index}")
                    cell_value = gameboard[row_index][column_index]
                    
                    if cell_value == "":
                        gameboard[row_index][column_index] = computersChoice
                        check_Won()
                        #checkDraw()
                        playerMove(player)
                        break
                    else:
                        checkDraw()
                        computer()
                    
                except (ValueError, IndexError):
                    computer()



        def main():
            playerMove(player)
        main()
game()