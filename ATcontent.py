#!/usr/bin/python

#1.- Asign the sequence to a variable
#2.- Count how many A's are in the sequence
#3.- Count how many T's are in the sequence
#4.- Sum the number of A's and the number of T's
#5.- Print the sum of A's and T's

seq1= ("ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT") #Asign the sequence to the variable seq1
ATcount= seq1.count ("A") + seq1.count("T") #Use count method for A and T, the + symbol will sum the number of A's and the number of T's
print(ATcount)
