""" Modules in python are the python files containing definitions and statements of the same
It contains the python functions, classes or variables
modules are saved with an extension .py
Module provides the flexibility and organize the code logically
It also provides reusability
"""

import math
import random as rd
import sys
import os
import salaryCalculator
import utility


"""
print(math.factorial(5))
aoc = 2*math.pi*math.pow(5,2)
print(aoc)
"""
"""
print(rd.random()) #random number between 0 to 1
#random number between 1 to 10
print("Random number between 1 to 10",math.floor(rd.random()*11))
print("Random number between 10 to 99 in steps of 10",rd.randrange(10,99,10))
print("Random number between 10 to 99 ",rd.randint(10,99))
"""
"""
print(sys.modules)
print(sys.path)
print(os.name)
print(os.getcwd())
"""

#print(dir(utility))
print(utility.isLeapYear(1900))
print("Preffered payment mode is",utility.payment_modes[1])
print ("Default Gender selected",utility.gender[2])

salaryCalculator.calculateSalary(20000)


