#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
### Convert seconds to hours, minutes and seconds ###
######################################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
given seconds s, convert to hours, minutes and seconds.
"""

def hconv(s) :   

    hrs = s // 3600
    hrs_rem = s % 3600
    mins = hrs_rem // 60
    secs = hrs_rem % 60
    print("{} seconds into hours, minutes and seconds is: ".format(s), end="")
    print("{}s --> {}h {}mn {}s".format(s,hrs,mins,secs))
    
if __name__ == '__main__':

    s = int(input("Please enter the number of seconds: "))
    hconv(s)