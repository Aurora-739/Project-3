# Project 3 - Tic Tac Toe

Tic Tac Toe is a Python terminal game, which runs in the Code Institute mock terminal Heroku.

Players play against the computer to win in this classic game of tic-tac-toe.

[Here is the link to the live version of this project](https://project-3-tic-tac-toe-3815fa166ad5.herokuapp.com/)

![image](https://github.com/user-attachments/assets/e6b049ba-711f-48f4-acf3-c696db426273)
The image above displays how the programme  will show up on different screen sizes. It is important to note that this is not how the programme looks at first and is instead how it looks after the player inputs their choice of "x" or "o".

## How to Play
Tic-Tac-Toe is based on the classic version of "tic-tac-toe" or "naughts and crosses" paper & pen game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe).

* In this version the player is prompted with the question, "Player, are you X or O?:" which allows them to input "x" or "o". (If something else is inputted e.g. an integer, a symbol or another letter, the code simply asks again until the player inputs an x or an o).
* The player goes first and is prompted with, "Choose your row between 0 & 2:" for where they want to put their "x" or "o" on the 3 by 3 grid.
* They are then asked, "Choose your column between 0 & 2:", for a precise location of where thy want their "x" or "o" on the 3 by 3 grid.
* Their guess is then marked on the grid.
* It is then the computer's turn. The computer places their "x" or "o" in an empty spot on the grid.
* This continues until there is an winner or until there are no spaces left which calls a draw.

## Features
### Existing Features

* Board generation
 * The board is the same every game (a 3 by 3 grid) and is generated at the first go of the player.
![image](https://github.com/user-attachments/assets/cbebb0b5-e4c7-4ecc-91c4-5f413607dc42)

* Play against the computer.
* Accepts user inputs

![image](https://github.com/user-attachments/assets/133f8180-0365-4d38-a9b6-07eb080d88bb)

* input validation and error checking:
  * If the space the user chooses is full, there is a check for a draw, and if not, then it calls an error and prints to the terminal, "Cell already taken, try again." And the user is given the opportunity to input another set of values.
  * If the player inputs a value that is not on the grid, e.g., row 0 and column 4, the error message "Invalid input, please try again" pops up, and the user is given the opportunity to input another set of values.
  
![image](https://github.com/user-attachments/assets/f26ae5da-3407-4dc2-b5cd-b34e570c4686)

