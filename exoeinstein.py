#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
### Law of addition of speeds ###
######################################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
TBD
"""
c = 300000

def einstein(u,v) :   
  
    return (u + v) / (1 + ((u * v)/(c * c)))
    
if __name__ == '__main__':

    u = 250000
    v = 290000
    print('{:.2f} + {:.2f} = {:.2f}'.format(u, v, einstein(u,v)))