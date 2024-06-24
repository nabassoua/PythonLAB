#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
### PYTHON. APPRENTISSAGE ACTIF (JP. ROY, EDITIONS ELLIPSES, 2020) ###
######################################################################

"""
turtle_init.py
Pour la fonction init(x,y,cap) entre autres...
"""

from turtle import *
from time import sleep
from math import pi, sqrt, sin, cos
from random import randint

def init(x=0,y=0,cap=0):
    '''Place la tortue au point (x,y) avec un cap absolu cap. 
    Le crayon est baissé, la tortue est cachée.'''
    ht() ; up() ; goto(x,y) ; down()
    setheading(cap)

def afficher(msg,x,y):
    '''Affiche le message msg centré au point (x,y) sans modifier
    la position de la tortue.'''
    M = pos() ; up() ; goto(x,y)
    write(msg,align='center',font=('Arial',24,'bold'))
    goto(M) ; down()
    
degré = pi/180      # valeur de 1 degré en radians

def deg_rad(ad):
    '''Prend un angle a en degrés et retourne sa mesure en radians.'''
    return ad * degré

def rot(M,K,ad):
    '''Retourne l'image du point M par la rotation de centre K
    et d'angle a en degrés.'''
    arad = deg_rad(ad)
    (c, s) = (cos(arad), sin(arad))
    (xK,yK) = K ; (xM,yM) = M
    xKM = xM - xK ; yKM = yM - yK
    return (xK + xKM * c - yKM * s, yK + xKM * s + yKM * c)

def segment(M1,M2):
    M = pos() ; up() ; goto(M1) ; down() ; goto(M2) ; up()
    goto(M)
    down()

if __name__ == '__main__':
    reset()
    init(0,0,90)   # cap Nord
    st()
    forward(200) ; afficher('M',0,205) ; back(200)
    orig = (0,0)
    segment(orig,rot((0,200),orig,45))
    mainloop()     # bloquant



