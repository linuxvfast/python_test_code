from random import randint

class Dice():
    '''骰子类'''
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        '''
        :return:返回骰子点数
        '''
        return randint(1,self.num_sides)

