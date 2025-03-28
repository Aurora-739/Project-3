from tabulate import tabulate 

gameboard = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

def printGameboard():
    print(tabulate(gameboard, headers =["Column 0", "Column 1", "Column 2"], tablefmt="rounded_grid", colalign=["center", "center", "center"])) 

    
def playersChoice():
    while True:
        player = input("Player, please choose, X or O for your go:\n").strip().upper()
        if player == "X" or player == "O":
            print(f"you have chosen {player.upper()}")
            break
        else:
                player = input("Player, please choose, X or O for your go:\n").strip().upper()
    return player

def playerMove():
    """
    where the player decides where to put their x / o
    """
    player = playersChoice()
    while True:
        try:
            row_index = int(input("Choose you row between 0 & 2:"))
            column_index = int(input("Choose your column between 0 & 2:"))
            cell_value = gameboard[row_index][column_index]
            
            if cell_value == "":
                gameboard[row_index][column_index] = player
                printGameboard()
                check_Won()
                break
            else:
                print("Cell already taken, try again.")
            
        except (ValueError, IndexError):
            print("Invalid input, please try again")

def check_Won():
    """
    looks at the data to see if the player / computer has 3 in a row
    """
    if 

def main():
    printGameboard()
    playerMove()
    check_Won()
main()