import random
import math
from enum import Enum

# class Shape(Enum):
#     CIRCLE="circle"
#     SQUARE="square"
    
#     def __str__(self):
#         return self.value

class Stimulus(object):

    shapes = ['circle', 'square']
    orientations = [45, 135] # was set to [0, 90] but it seems to give me 45 degrees off
    adjust = [-22.5, 22.5]
    colors = ['green', 'red']
    lineWidth = 3 #px
    
    def __init__(self, distractor=False, shape='', orientation=0, color=''):
        self.distractor = distractor
        self.shape = 'circle'
        self.orientation = random.choice(self.orientations) + random.choice(self.adjust)
        self.color = color

    @property
    def shape(self):
        return self._shape
    @shape.setter
    def shape(self, val):
        self._shape = val
        self.orientation = random.choice(self.orientations)

    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, val):
        self._position = val
    
    def __str__(self):
        return "Distractor: {0}\nShape: {1}\nOrientation: {2}\nColor: {3}\nPosition: {4}\n".format(
            self.distractor,
            self.shape,
            self.orientation,
            self.color,
            self.position
            )