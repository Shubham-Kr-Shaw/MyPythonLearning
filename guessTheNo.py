#This is a game program
import random
num = random.randint(0,100)
chance = 1
print("You have only 10 chances to win.")

while (chance<=9):
    guess = int(input("Guess the no:\n"))
    if guess<num:
        print("you enter less number please input greater number.\n")
    elif guess>num:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(chance,"no.of guesses he took to finish.")
        break
    print(9-chance,"no. of guesses left")
    chance = chance + 1

if(chance>9):
    print("Game Over")
