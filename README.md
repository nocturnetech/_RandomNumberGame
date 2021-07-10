# _RandomNumberGame

This is a simple game where the the user needs to guess a random number

First the console will request to enter the persons username and age. It varifies the age (18+) and starts the game.
The program makes sure the entered age is a number 

A random number is generated and the user needs to guess it. If guessed correctly -> user receives 10 points.

After every guessed or missed number the program asks if the user would like to quit. 
If the answer is yes the game asks if the user would like to save the points to scores.txt file. 

If the user decides to save the score and the file does not exist then the program will create it. 
Otherwise the score is placed on the existing file not overwriting the previous scores
