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
    orientations = [0, 90]
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
        origin = self.position
        print('origin', origin)
        angle = self.orientation

        x1 = origin[0] - 0.05
        y1 = origin[0]
        x2 = origin[1] + 0.05
        y2 = origin[1]
        self._line_coordinates = [(x1, y1), (x2, y2)]
        
        # if angle in {0, 90}:
        #     print('0 or 90')
        #     if angle == 0:
        #         x1 = origin[0] - 0.1
        #         y1 = origin[0]
        #         x2 = origin[1] + 0.1
        #         y2 = origin[1]
        #         self._line_coordinates = [(x1, y1), (x2, y2)]
        #     else:
        #         x1 = origin[0]
        #         y1 = origin[0] + 0.1
        #         x2 = origin[1]
        #         y2 = origin[1] - 0.1
        #         self._line_coordinates = [(x1, y1), (x2, y2)]
        # elif angle in {-22.5, 22.5, 67.5}:
        #     print('22.5, -22.5, or 67.5')
        #     x1 = origin[0] + 0.1 * math.cos(angle)
        #     y1 = origin[0] + 0.1 * math.sin(angle)
        #     x2 = origin[1] - 0.1 * math.cos(angle)
        #     y2 = origin[1] - 1.1 * math.sin(angle)
        #     self._line_coordinates = [(x1, y1), (x2, y2)]
        # elif angle in {112.5}:
        #     print('67.5 or 112.5')
        #     adjusted_angle = 180 - angle
        #     x1 = origin[0] + 0.1 * math.cos(adjusted_angle)
        #     y1 = origin[0] + 0.1 * math.sin(adjusted_angle)
        #     x2 = origin[1] - 0.1 * math.cos(adjusted_angle)
        #     y2 = origin[1] - 0.1 * math.sin(adjusted_angle)
        #     self._line_coordinates = [(x1, y1), (x2, y2)]
    
    @property
    def line_coordinates(self):
        return self._line_coordinates
    
    def __str__(self):
        return "Distractor: {0}\nShape: {1}\nOrientation: {2}\nColor: {3}\nPosition: {4}\nLine: {5}\n".format(
            self.distractor,
            self.shape,
            self.orientation,
            self.color,
            self.position,
            self.line_coordinates
            )