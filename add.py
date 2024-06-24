#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
### Add 2 integers ###
######################################################################

"""
returns the result of x+y
"""

def add(x,y) :
    res = x+y
    print("The answer is:{} ".format(res))

if __name__ == '__main__':
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    add(x,y)
