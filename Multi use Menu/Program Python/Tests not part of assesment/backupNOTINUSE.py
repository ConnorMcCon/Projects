#Connor McConaghy
#03/03/2021
#Python
#Gives three options 1. generate a username 2. calculate the factorial of a number 3. Exit the program

import math

#----------------------------------------Functions--------------------------------------------------------

#Writing out funtions too call on later on.
#menu interface funtion
def validMenuOption():
    print("\n")
    print("Welcome to the EPOS options Ltd.")
    print("Network Administration and Statistics Department's")
    print("Pilot 'One Stop Shop' interface\n")
    print("Please type the number of one of the following menu options\n")
    print("Option 1:   To generate a personal username")
    print("Option 2:   To calculate a number's factorial")
    print("Option 3:   To exit the application\n")
    global numberIn
    numberIn = int(input("- "))         #getting an input and storing it
    while numberIn >=4:                 #if the number 4 is entered this executes
        print("\nYou entered an invalid menu choice, only the options '1', '2' and '3' are allowed, please try again.")
        return validMenuOption()
        

#Gets the names that the user enters
def getNames():
    print("We will generate a personal username using your Forename and Surname\n")
    forename=input("Please enter Forename - ")                                              #storing user input in the varibles forename and surname
    surname=input("Please enter Surname - ")
    createUsername(forename, surname)

#Creates a username and stores it in username varible
def createUsername(forename, surname):
    username=forename[0] + surname
    showUsername(username)

#Prints the username varible with text and returns to main menu function
def showUsername(username):                                                                         #to create a username by the string manipulation of the inputs entered
    print("The network username to be used is",username)                                    
    return validMenuOption()



#Calculating factorial number function
def calculateFactorial():
    print("We will calculate the factorial of the number you enter")
    global number, factorial
    number=int(input("Please enter number - "))
    factorial=(math.factorial(number))

#prints out number and factorial with text then returns to main menu function
def displayFactorial():
    print("The factorial of",number,"is",factorial)
    return validMenuOption()
    


#---------------------------------------- start of program -----------------------------------------------

#start of menu option
validMenuOption()


#start of generate username.
while numberIn == 1:
    getNames()
    createUsername()
    showUsername()

            
#start of calculate factorial of a number entered by the user
while numberIn == 2:
    calculateFactorial()
    displayFactorial()

#An exit command if the number entered is 3
while numberIn == 3:
    print("You have exited the program")
    break
