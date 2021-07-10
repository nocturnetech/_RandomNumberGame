from random import randint

def saveScore ():
    strPoints = str(points)
    f = open ("scores.txt", "a")
    f.write ("|Username: " + username + "||Score: " + strPoints + "|\n")
    f.flush()
    
username = input ("Please enter your username:\n")
age = input ("Please enter your age:\n")
error = 0

try:
    intAge = int (age)

    if intAge >= 18:
        end = 1
        points = 0

        print ("You are of legal age to play this game")
        while end !=0:
                    
            number = randint(1, 9)
            print ("Random number: %d" %(number))
            inputNumber = input ("Guess the number between 1 and 9:\n")
            intNumber = int (inputNumber)

            if number == intNumber:
                print ("Correct! + 10 points!")
                points += 10
            else:
                print ("Better luck next time :)")

            answer = input ("Would you like to continue? y/n?\n")
                    
            if answer == "n":
                answer2 = input("Would you like to save your score to score.txt file? y/n?\n")
                if answer2 == "y":
                    saveScore()
                            
                print ("Thank you for playing!")
                end = 0
                    
    else:
            print ("You are too young to play this game")
except ValueError:
    print ("Error: You did not enter a number")
        
        



