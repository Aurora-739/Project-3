from tabulate import tabulate 

gameboard = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
print(tabulate(gameboard, tablefmt="rounded_grid")) # add tabulate headers.

    
def playersChoice():
    while True:
        player = input("Player, please choose, X or O for your go:\n").strip().upper()
        if player == "X" or player == "O":
            print(f"you have chosen {player.upper()}")
            break
        else:
                player = input("Player, please choose, X or O for your go:\n").strip().upper()

def PlayerMove():
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
                cell_value = player
                break
            else:
                print("Cell already taken, try again.")
                return False
            
        except (ValueError, IndexError):
            print("Invalid input, please try again")
            return False


def main():
    PlayerMove()
main()