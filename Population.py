#!/usr/bin/python

"""
This pipeline computes population estimation
"""

years= input("How many years you want to estimate?\n")
int(years)

#There are 86400 seconds in a day

initial_pop=307357870
int(initial_pop)
births=(86400*7)*365 #Number of births in one year
immigrants=(86400*35)*365 #Number of immigrants in one year
death=(86400*13)*365 #Number of deaths in one year

final_pop=initial_pop+((births+immigrants)-death)*years
int(final_pop)

print 'The population size in', years, 'years will be', final_pop
