#Connor McConaghy
#Dice Rolling Simulator

import random

numberlist = range(1,7)

while True:
    diceroll = random.choice(numberlist)
    user = input("Type 'r' to roll the dice - ")
    if user == "r":
        print(diceroll)
    else: break
    
