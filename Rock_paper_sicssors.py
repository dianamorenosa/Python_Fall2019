#!/usr/bin/python

import random
options = ["Rock", "Paper", "Scissors"]
computer = random.choice(options)


user=raw_input("Rock, Paper or Scissors? \n")

print ("You chose"), user 

print ("I chose"), computer, "\n"


if (computer=="Rock" and user=="Paper"):
	print("You Win!!")
elif (computer=="Scissors" and user=="Rock"):
	print("You Win!!")
elif (computer=="Paper" and user=="Scissors"):
	print("You Win!!")
elif (computer==user):
	print("Is a tie")
else:
	print("You lose :(")
