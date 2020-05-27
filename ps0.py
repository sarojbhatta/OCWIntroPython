# -*- coding: utf-8 -*-
"""
Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.
"""
import numpy

x = int(input("Enter number x:"))
y= int(input("Enter number y:"))
powval = x**y
print("X**Y = " + str(powval))
logval = numpy.log2(x)
print("log(x) = " + str(logval))