#===============================================================================
# Created by Ben Pham
#===============================================================================
# 2 possible algorithms where x is the number going through the algorithms
#     - x*0 + y
#             - y is [0,1]
#     - x/y
#             - y is [2,4]
#===============================================================================

from random import choice
from random import randint

def return_algorithm():
    ''' Returns the algorithm to use '''
    select_int1 = randint(0,1)
    select_int2 = randint(2,4)
    
    select1 = [lambda x: x*0 + select_int1]
    select2 = [lambda x: x/select_int2]
    
    return choice((select1,select2))
