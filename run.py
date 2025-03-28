from tabulate import tabulate 

gameboard = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
print(tabulate(gameboard, tablefmt="rounded_grid"))