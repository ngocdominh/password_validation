# Build a program to create a number guessing game.
#
# Requirements:
#
# 1. The program will automatically generate a random number between 1 and 100.
# 2. Prompt the player to input a number for their guess.
# 3. Display a message if the guessed number is higher or lower than the random number and indicate the remaining guess count.
# 4. When the player correctly guesses the number, display the number of guesses needed and notify them that they guessed correctly.
# 5. After each guessing round, ask the player if they want to play again. If yes, generate a new random number and restart the game.


import random
# import numpy

def guessing_game():
    machine = random.randint(0, 100)
    cnt = 5

    while cnt > 0:
        human = input("Enter your number: ")
        human = int(human)
        cnt = cnt - 1
        if human < machine:
            print("Your number is lower than the machine's one. You have " + str(cnt) + " time(s) left")
        elif human > machine:
            print("Your number is higher than the machine's one. You have " + str(cnt) + " time(s) left")
        else:
            print("Perfect! You've got the right number")

    if cnt == 0:
        print("Sorry, the correct number is " + str(machine))


while True:
    a = input(" Do you want to play another round? (Y/N): ")
    if a.upper() == 'N':
        break
    elif a.upper() == 'Y':
        continue
        guessing_game()


