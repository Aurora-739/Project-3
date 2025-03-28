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

def check_Won(row):
    """
    looks at the row to see if the player / computer has 3 in a row
    """
    for row in gameboard:
        if row[0] != "0" and row[0] == row[1] == row[2]:
            return True
        
    for col in range(3);
        if gameboard[0][col] == gameboard[1][col] == gameboard[2][col]
    
def check_Won():
    """
    looks at the gameboard to see if theres any in common
    """
    for i, row in enumerate(gameboard):
        if check_Won(row):
            print(f"Row {i+1} has 3 of the same value!")
        else:
            print(f"Row {i+1} does not have 3 of the same value.")

def main():
    printGameboard()
    playerMove()
    check_Won()
main()