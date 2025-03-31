# Project 3 - Tic Tac Toe

Tic Tac Toe is a Python terminal game, which runs in the Code Institute mock terminal Heroku.

Players play against the computer to win in this classic game of tic-tac-toe.

[Here is the link to the live version of this project](https://project-3-tic-tac-toe-3815fa166ad5.herokuapp.com/)

![image](https://github.com/user-attachments/assets/e6b049ba-711f-48f4-acf3-c696db426273)
The image above displays how the programme  will show up on different screen sizes. It is important to note that this is not how the programme looks at first and is instead how it looks after the player inputs their choice of "x" or "o".

## How to Play
Tic-Tac-Toe is based on the classic version of "tic-tac-toe" or "naughts and crosses" paper & pen game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe).

* In this version the player is prompted with the question, "Player, are you X or O?:" which allows them to input "x" or "o". (if something else is inputted e.g. an integer, a symbol or another letter, the code simply asks again until the player inputs an x or an o).
* The player then is prompted with, "Choose your row between 0 & 2:" for where they want to put their "x" or "o" on the 3 by 3 grid.
* They are then asked, "Choose your column between 0 & 2:", for a precise location of where thy want their "x" or "o" on the 3 by 3 grid.
* Their guess is then marked on the grid.
* It is then the computer's turn. The computer places their "x" or "o" in an empty spot on the grid.
* This continues until there is an winner or until there are no spaces left which calls a draw.

## Features

  * If the spot is open on the grid then the "x" or "o" is places there, if not then there is a check for a draw and if not then it calls an error and prints to the terminal: "Cell already taken, try again.".
  * 
