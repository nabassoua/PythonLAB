#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
### Returns the bigger number in absolute value term ###
######################################################################

"""
FILL ME IN
"""

def max_abs(x,y) :

    if x==y:
        return x
    elif abs(x) < abs(y):
        return y
    else:
        return x

if __name__ == '__main__':

    x = int(input("Enter a number: "))
    y = int(input("Enter a second number: "))
    print("The bigger number in absolute value term is: ",max_abs(x,y))
