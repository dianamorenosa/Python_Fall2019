#!/usr/bin/python


#Guess the number game:

#1.- Use random to ask the computer to randomly chose a number from 1 to 50
#2.- Use input for asking user to guess the number
#3.- Set a loop where if user's input is not the same as computer the game will give some hints about the real number
#4.- Loop will stop once the user guess the right number

import random

computer = random.randrange(51) #Ask the computer to chose a number from 1 to 50

guess= input("From 1 to 50, which number I am thinking on?\n") #Asign to "guess" variable the input number

user=int(guess) #Make the input an integer and asign it to a new variable
 

while computer!=user: 					
	if computer > user:
		guess2= input("I am thinking in a higher number, try again \n") #give another try with a higher number, this will replace the original user number
		user=int(guess2) #Again I have to change the variable guess2 to an integer and save it in "user" variable to re-enter into the loop, this new value will replace the original in line 15.
	elif computer < user:
		guess3= input("I am thinking in a lower number, try again \n") #give another try with a lower number, this will replace the previous user number
		user=int(guess3)
else:
	print ("You are right! I was thinking in", computer) #In this case else will be that computer==user, the loop ends here.
	


 

