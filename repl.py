import math
import numpy as np
from stim import Stimulus

# stimulus_array = [Stimulus() for _ in range(5)]

# def printContents():
#     for i in stimulus_array:
#         print(i, '\n')

# setattr(stimulus_array[0], 'shape', 'square')
# print(stimulus_array[0])














def polygon(sides, radius=6, rotation=0, translation=None):
    one_segment = math.pi * 2 / sides
    points = [
        (math.sin(one_segment * i + rotation) * radius,
         math.cos(one_segment * i + rotation) * radius)
        for i in range(sides)]
    if translation:
        points = [[sum(pair) for pair in zip(point, translation)] for point in points]
    return points

# print(polygon(5)[0])















def setattrs(_self, **kwargs):
    for k,v in kwargs.items():
        setattr(_self, k, v)

# setattrs(stimulus_array[0], shape='square', color='red') 
# print(stimulus_array[0])

# print(stimulus_array.index(np.random.choice([item for item in stimulus_array if item.distractor == False])))













def create_distribution(size):
    distractors_matched = distractors_mismatched = int(size * 0.25)
    nondistractors = size - (distractors_matched + distractors_mismatched)
    # print('distractors:', distractors_matched)
    # print('distractors_mismatched:', distractors_mismatched)
    # print('nondistractors:', nondistractors)
    arr = np.array([0] * int(nondistractors) + [1] * int(distractors_matched) + [2] * int(distractors_mismatched))
    np.random.shuffle(arr)
    return arr

# print(create_distribution(600))









# x = Stimulus()
# print(x.color, x.orientation)
# setattr(x, 'shape', 'square')
# print(x.shape, x.orientation)










# for i in stimulus_array:
#     print(i.shape, i.orientation, i.distractor)

# stimulus_array[0].distractor = True
# stimulus_array[2].shape = 'square'
# print('')

# itemToChange = [x for x in stimulus_array if x.distractor == True][0]
# targetItem = [x for x in stimulus_array if x.shape == 'square'][0]
# itemToChange.orientation = targetItem.orientation

# for i in stimulus_array:
#     print(i.shape, i.orientation, i.distractor)

# print('\ntarget index', stimulus_array.index(targetItem))


















origin = (0, 0)
radius = 3

x = Stimulus()
x.shape = 'square'
x.position = (20, 20)
print('position:', x.position)
print('line coords:', x.line_coordinates)