#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
### FILL ME IN ###
######################################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
### PYTHON. APPRENTISSAGE ACTIF (JP. ROY, EDITIONS ELLIPSES, 2020) ###
######################################################################

"""
exo_dragon.py (11.56)
Une jolie courbe fractale...
"""

from turtle_init import *         # cf ci-dessous
# init(x=0,y=0,cap=0)
# afficher(msg,x,y)
# sleep(dt)            en secondes flottantes
# deg_rad(a_degres)    conversion degrés -> radians
# rot(M,K,a_degres)    K = centre de rotation
# segment(M1,M2)       le tracé
# pi, sqrt, sin, cos, randint   pour les calculs fréquents

from math import sqrt

def dragon(n,T) :       # T = distance du point de départ au point d'arrivée
    if n == 0 :
        forward(T)      # le générateur
    else :
        left(45)
        dragon(n-1, T/sqrt(2))
        right(90)       # axe de symétrie dans le dessin et dans le code...
        dragon(n-1, T/sqrt(2))
        left(45)


tracer(True)            # lent !
speed('fastest')
for n in range(1,7):
    clear()                 # efface le canevas sans recentrer la tortue
    afficher('Courbe du Dragon',0,230)
    afficher('(niveau {}, "fastest")'.format(n),0,195)
    init(-125,-100,0)
    st()
    dragon(n,250)
    sleep(1)
tracer(False)           # rapide !
clear()
afficher('Courbe du Dragon',0,230) ; afficher('(niveau 13, rapide)',0,195)
init(-125,-100,0)
st()
dragon(13,250)
tracer(True)

getcanvas().postscript(file='dragon.ps')     # pour avoir un fichier image du canevas

mainloop()            # pour une exécution au Terminal
print('Fini')

# COMPLEMENTS EN LIGNE
from webbrowser import open as browse
#browse('https://fr.wikipedia.org/wiki/Fractale')
#browse('https://fr.wikipedia.org/wiki/Courbe_du_dragon')