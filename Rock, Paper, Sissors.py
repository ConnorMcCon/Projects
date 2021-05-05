#Rock, Paper, Sissors

import random

gamelist = ["Rock","Paper","Sissors"]

while True:
    computer = random.choice(gamelist)
    user = input("Type Rock, Paper, or Sissors - ")
    
    if user == "Rock" and computer == "Sissors":
        print("You Win")
    if user == "Paper" and computer == "Rock":
        print("You Win")
    if user == "Sissors" and computer == "Paper":
        print("You Win")
        
    if user == "Rock" and computer == "Paper":
        print("You Lose")
    if user == "Paper" and computer == "Sissors":
        print("You Lose")
    if user == "Sissors" and computer == "Rock":
        print("You Lose")

    if user == "Rock" and computer == "Rock":
        print("You Drew")
    if user == "Paper" and computer == "Paper":
        print("You Drew")
    if user == "Sissors" and computer == "Sissors":
        print("You Drew")


#tests
#Type Rock, Paper, or Sissors - Rock
#You Win
#Type Rock, Paper, or Sissors - Sissors
#You Lose
#Type Rock, Paper, or Sissors - Paper
#You Win
