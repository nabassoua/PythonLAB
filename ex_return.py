#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
### returns the sum of the 2 largest numbers given 3 numbers ###
######################################################################

"""
a,b,c are user inputs
"""

def sommecar_2max(a,b,c) :

    print("The sum of the 2 largest numbers is: \n")
    
    min1 = min(a,b,c)
    sum = 0
    
    if min1 <= a:
        sum = b+c
    elif min1 <= b:
        sum = a + c
    else:
        sum = a + b
        
    return sum      
    
if __name__ == '__main__':
    a=int(input("Please enter your first number: "))
    b=int(input("Please enter your first number: "))
    c=int(input("Please enter your first number: "))
    sommecar_2max(a,b,c)