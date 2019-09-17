#!/usr/bin/python

"""
This pipeline corresponds to the third homework
"""
import random
bases = ["A", "C", "T", "G"]
sequence = random.choices(bases, k=100)


#How many G's are in the sequence?
sequence.count ("G")

#How many C's are in the sequence?
sequence.count ("C") 

#How many A's and C's combined are in the sequence?
sequence.count ("G") + sequence.count("A")
