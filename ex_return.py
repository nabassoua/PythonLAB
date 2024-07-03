#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
### returns the sum of the 2 largest numbers given 3 numbers ###
######################################################################

"""
a,b,c are user inputs
"""

def sommecar_2max(a,b,c) :

   if a < b: 
       if c < a: return a * a + b * b
       else: return b * b + c * c
   else:
       if c < b: return a * a + b * b
       else: return a * a + c * c
    
if __name__ == '__main__':
    a=int(input("Please enter your first number: "))
    b=int(input("Please enter your first number: "))
    c=int(input("Please enter your first number: "))
    print("The sum of the 2 largest numbers is: ", end="")
    print(sommecar_2max(a,b,c))