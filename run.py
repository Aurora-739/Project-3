from tabulate import tabulate 
import random

gameboard = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
def game():
    
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
                for row in gameboard:
                    """
                    checks rows
                    """
                    if row[0] != "" and row[0] == row[1] == row[2]:
                        break
                    
                for col in range(3):
                    """
                    check columns
                    """
                    if gameboard[0][col] == gameboard[1][col] == gameboard[2][col] and gameboard[0][col] != "":
                        #print("YOU WON!!!")
                        return False
                
                if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] and gameboard[0][0] != "":
                    """
                    Checks diagonal (top left to bot. right)
                    """
                    #print("YOU WON!!!")
                    return False
                if gameboard[0][2] == gameboard[1][1] == gameboard[2][0] and gameboard[0][0] != "":
                    """
                    Checks diagonal (top right to bot. left)
                    """
                    #print("YOU WON!!!")
                    return False

                return True
                
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
                        checkDraw()
                        computer()
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
                    print("Computer's Turn...")
                    row_index = random.randint(0,2)
                    column_index = random.randint(0,2)
                    print(f"Computer plays: row: {row_index} & column: {column_index}")
                    cell_value = gameboard[row_index][column_index]
                    
                    if cell_value == "":
                        gameboard[row_index][column_index] = computersChoice
                        check_Won()
                        checkDraw()
                        playerMove(player)
                        break
                    else:
                        computer()
                    
                except (ValueError, IndexError):
                    computer()



        def main():
            playerMove(player)
        main()
game()