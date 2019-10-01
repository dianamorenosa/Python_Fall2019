#!/usr/bin/python

#1. Asign the sequence to a variable
#2. Cut the sequence when it finds the motif GAATTC, the position where EcoRI cuts is between G and A.
#3. Calculate the length of the splitted sequences

dnaseq = ("ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT") #Asign DNA sequence to a variable

restriction = ("G AATTC") #Make a variable with the restriction sequence already splitted 

dnaseq2 = dnaseq.replace("GAATTC", restriction) #Replace the regions that contains the motif by the splitted one in restriction variable.

cutseq= dnaseq2.split(" ") #SPlit the sequence by space
print (cutseq[0]) #Corroborate that the sequence splits correctly 
print (cutseq[1])

seq1=len(cutseq[0]) #Calculate the lenght of the first sequence
print ("The lenght of the first fragment is", seq1, "bp")

seq2=len(cutseq[1]) #Calculate the lenght of the second sequence
print ("The lenght of the first fragment is", seq2, "bp")



