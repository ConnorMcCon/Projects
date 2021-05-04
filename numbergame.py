#Number game

import random

numberlist = range(1,100)
randomnumber=random.choice(numberlist)


def NumberSolution():
    while True:
        guess = int(input("Guess a number between 1-100 - "))
        if guess < randomnumber:
            print("Number is higher")
        else:
            print("Number is less")
        if guess == randomnumber:
            print("You guessed correctly")
            break

NumberSolution()


    



