#===============================================================================
# NumbeRand
# Created on Aug 30, 2014
# 
# @author: Ben Pham
#
# Handles the level you are in
#    - You got 100% chance to get it right on Level 1. 
#    - Bound 1,000,000 is correct.
#    - Bound 500,000 on Level 2.
#    - Continuously half the range you must be in for each number after each
#        level to advance.
#            * If you are out of the range, you lose
#===============================================================================
from random import randint


class GameLogic():
    MAX = 999999
    MIN = 0
    
    def __init__(self, algorithm):
        self.level = 0
        self.bound = GameLogic.MAX + 1
        self.number = randint(GameLogic.MIN,GameLogic.MAX)
        self.history = [self.number]
        self.algorithm = algorithm
        self.bound_proximity()
        
    
    def bound_proximity(self):
        ''' Generate numbers to see how close you are to the bound '''
        self.very_hot = self.number-(self.bound*0.01), self.number+(self.bound*0.01)        
        self.hot = self.number-(self.bound*0.05), self.number+(self.bound*0.05)             
        self.warmer = self.number-(self.bound*0.1), self.number+(self.bound*0.1)          
        self.warm = self.number-(self.bound*0.25), self.number+(self.bound*0.25)
        
        
    def check_bound(self, num: int):
        ''' Make sure that the chosen number is within bounds '''
        if num == self.number:
            return "EXACT"
        elif num > self.very_hot[0] and num < self.very_hot[1]:
            return "VERY HOT"
        elif num > self.hot[0] and num < self.hot[1]:
            return "HOT"
        elif num > self.warmer[0] and num < self.warmer[1]:
            return "WARMER"
        elif num > self.warm[0] and num < self.warm[1]:
            return "WARM"
        elif num > self.number - self.bound and num < self.number + self.bound:
            return "OK"
        return "LOSE"
        
    
    def victory(self, num: int):
        ''' Final Check if bounds are 0, you must get exact number to win '''
        return self.check_bound(num) == 'EXACT' and self.return_bound() == 0
    
        
    def next_level(self):
        ''' 
        - Advance to next level 
        - Half the bound
        '''
        self.level += 1
        self.bound = round(self.bound/2)
        self.number = round(self.algorithm[0](self.number)%(GameLogic.MAX+1))
        self.algorithm = self.algorithm[1:] + self.algorithm[:1]
        self.history.append(self.number)
        self.bound_proximity()
        
        
    def return_level(self):
        return self.level
    
    
    def return_bound(self):
        return self.bound
    
    
    def return_number(self):
        return self.number
    
    
    def return_history_as_str(self):
        return str(self.history).lstrip("'[").rstrip("]'")
