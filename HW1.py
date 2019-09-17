#!/usr/bin/python

"""
This pipeline corresponds to the first homework
"""

#Set the string for each species

Efuscus = "Eptesicus fuscus"
Maus= "Myotis austroriparius"
Msep= "Myotis septentrionalis"

#Make a second string with the correct abreviations of each species

Ef=Efuscus[0:3] + Efuscus[10:13]
Ma=Maus[0:3] + Maus[7:10]
Ms=Msep [0:3] + Msep[0:3]



print ("There are three species of bats:\n", Ef.upper(), "\n", Ma.upper(), "\n", Ms.upper())

