from tabulate import tabulate 
import random



def game():
    gameboard = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    def printGameboard():
                print(tabulate(gameboard, headers =["Column 0", "Column 1", "Column 2"], tablefmt="rounded_grid", colalign=["center", "center", "center"]))

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
            exit
         
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
                #return win
            if gameboard[0][2] == gameboard[1][1] == gameboard[2][0] == player:
                    """
                    Checks diagonal (top right to bot. left)
                    """
                    win = True
                    #return win

            if win == True:
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
                        if check_Won():
                            return True
                        if checkDraw():
                            return True
                        computer()
                        break
                    else:
                        if check_Won():
                            return True
                        if checkDraw():
                            return True
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
                    row_index = random.randint(0,2)
                    column_index = random.randint(0,2)
                    cell_value = gameboard[row_index][column_index]
                    
                    if cell_value == "":
                        gameboard[row_index][column_index] = computersChoice
                        print("Computer's Turn...")
                        print(f"Computer plays: row: {row_index} & column: {column_index}")
                        if check_Won():
                            return True
                        if checkDraw():
                            return True
                        playerMove(player)
                        break
                    else:
                        if check_Won():
                            return True
                        if checkDraw():
                            return True
                        computer()
                    
                except (ValueError, IndexError):
                    computer()



        def main():
            playerMove(player)
        main()
game()