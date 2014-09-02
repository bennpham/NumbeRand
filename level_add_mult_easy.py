#===============================================================================
# Created by Ben Pham
#===============================================================================
# 2 possible algorithms where x is the number going through the algorithms
#    - x + y
#            - y is [-5,5]
#     - x * y
#            - y is [0,5]
#===============================================================================

from random import choice
from random import randint


def return_algorithm():
    ''' Returns the algorithm to use '''
    easy_int1 = randint(-5,5); easy_int2 = randint(0,5) 
    
    easy1 = [lambda x: x + easy_int1]
    easy2 = [lambda x: x * easy_int2]
    
    return choice((easy1, easy2))
