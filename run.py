from tabulate import tabulate 

gameboard = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(tabulate(gameboard, tablefmt="rounded_grid"))

#def PlayersChoice():
   # print("Would you like to be X or O?")
   # if "x":
def checkEmpty(search_item):
    """
    Checks if the location on the board where the player wants to place their X is free
    If it's free, it allows the player to place it there and passes it to the function to see if they've got three in a row"""
    try:
        value = # this value needs to be equal to the location on the gameboard where the player is requesting to place their item.
        if value == search_item:
            #replace the value in the board with the search item (X)
        else:
            return False
    except IndexError:
        print(f"Invalid row or column index. Ensure you're using a valid index.")
        return False1
    


def PlayerMove():
    while True:
        try:
            search_item = input("Choose your position based on the numbers:\n")
            checkEmpty(search_item)
            
        except (ValueError, IndexError):
            print("Invalid input, please try again")
            return False


def main():
    PlayerMove()
    checkEmpty()
main()