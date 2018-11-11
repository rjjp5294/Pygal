from random import randint

class Die():
    '''Class to represent a single die'''

    def __init__(self, num_sides=6):
        '''Assuming a 6-sided die'''
        self.num_sides = num_sides

    def roll(self):
        '''Returns random value between 1 and the number of sides of the die'''
        return randint(1, self.num_sides)
